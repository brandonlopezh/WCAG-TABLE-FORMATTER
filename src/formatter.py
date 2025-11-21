def add_wcag_styles(html_table):
    from bs4 import BeautifulSoup
    import re

    # Parse the HTML table
    soup = BeautifulSoup(html_table, 'html.parser')
    
    # Fix header levels - change h3 to h2
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for header in headers:
        if header.name == 'h3':
            new_h2 = soup.new_tag('h2')
            new_h2.string = header.get_text(strip=True)
            # Copy attributes if any
            for attr, value in header.attrs.items():
                new_h2[attr] = value
            header.replace_with(new_h2)
    
    # Find all tables in the content
    tables = soup.find_all('table')
    
    if not tables:
        return html_table  # Return original if no tables found

    for table in tables:
        # Update table attributes - add class and remove cellpadding/cellspacing
        table.attrs = {'class': 'table', 'border': '1'}
        
        # Create tbody wrapper
        tbody = soup.new_tag('tbody')
        
        rows = table.find_all('tr')
        
        if not rows:
            continue
            
        # Move all rows into tbody
        for row in rows:
            row.extract()  # Remove from table
            tbody.append(row)  # Add to tbody
            
        # Add tbody to table
        table.append(tbody)
        
        # Clean up text content in cells and detect header patterns
        for row in tbody.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            for cell in cells:
                # Clean up nested p tags and formatting
                if cell.find('p'):
                    # Extract text from p tags and clean up
                    text_content = cell.get_text(strip=True)
                    cell.clear()
                    cell.string = text_content
                elif cell.find(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
                    # Extract text from header tags
                    text_content = cell.get_text(strip=True)
                    cell.clear()
                    cell.string = text_content
        
        rows = tbody.find_all('tr')  # Get rows from tbody now
        
        # Process first row - convert to headers if they look like headers
        if rows:
            first_row = rows[0]
            cells = first_row.find_all(['td', 'th'])
            
            for cell in cells:
                if cell.name == 'td':
                    # Check if this looks like a header (bold text, short content, etc.)
                    text = cell.get_text(strip=True)
                    if (text and (len(text) < 50 or 
                        any(keyword in text.lower() for keyword in ['engine', 'transmission', 'features', 'wheels', 'lights', 'seating']) or
                        text.isupper() or 'strong' in str(cell))):
                        
                        # Convert to th with proper scope
                        new_th = soup.new_tag('th')
                        new_th.string = text
                        
                        # Determine scope based on colspan
                        if cell.get('colspan'):
                            new_th['scope'] = 'colgroup'
                            new_th['colspan'] = cell['colspan']
                        else:
                            new_th['scope'] = 'col'
                        
                        # Copy other attributes except colspan (already handled)
                        for attr, value in cell.attrs.items():
                            if attr not in ['colspan']:
                                new_th[attr] = value
                                
                        cell.replace_with(new_th)
                        
                elif cell.name == 'th':
                    # Add scope if missing
                    if 'scope' not in cell.attrs:
                        if cell.get('colspan'):
                            cell['scope'] = 'colgroup'
                        else:
                            cell['scope'] = 'col'

        # Process remaining rows
        for row in rows[1:]:
            cells = row.find_all(['td', 'th'])
            if cells:
                first_cell = cells[0]
                
                # Convert first cell to row header if it looks like a label
                if first_cell.name == 'td':
                    text = first_cell.get_text(strip=True)
                    
                    # Check if this looks like a row header
                    if (text and not text.isdigit() and 
                        not text in ['-', 'S', 'O', 'A'] and
                        len(text) > 1):
                        
                        new_th = soup.new_tag('th')
                        new_th.string = text
                        new_th['scope'] = 'row'
                        
                        # Copy attributes
                        for attr, value in first_cell.attrs.items():
                            new_th[attr] = value
                            
                        first_cell.replace_with(new_th)

    # Clean up the final output - remove extra whitespace
    output = str(soup)
    
    # Remove excessive whitespace between tags
    output = re.sub(r'>\s+<', '><', output)
    
    # Clean up line breaks and spaces in table content
    output = re.sub(r'\n\s*\n', '\n', output)
    
    # Format with proper indentation for readability
    output = output.replace('><tbody><tr>', '>\n<tbody>\n<tr>')
    output = output.replace('</tr><tr>', '</tr>\n<tr>')
    output = output.replace('</tbody></table>', '</tbody>\n</table>')
    
    return output

# Example usage
if __name__ == "__main__":
    sample_html = """
    <h3>Mechanical</h3>
    <table border="1" cellspacing="0" cellpadding="0" width="638">
        <tr>
            <td>Name</td>
            <td>Age</td>
            <td>City</td>
        </tr>
        <tr>
            <td>John</td>
            <td>25</td>
            <td>NYC</td>
        </tr>
    </table>
    """
    formatted_html = add_wcag_styles(sample_html)
    print(formatted_html)