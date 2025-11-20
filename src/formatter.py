def add_wcag_styles(html_table):
    from bs4 import BeautifulSoup

    # Parse the HTML table
    soup = BeautifulSoup(html_table, 'html.parser')
    table = soup.find('table')

    if not table:
        return html_table  # Return original if no table found

    rows = table.find_all('tr')
    
    # Process first row - likely column headers
    if rows:
        first_row = rows[0]
        cells = first_row.find_all(['td', 'th'])
        
        for cell in cells:
            if cell.name == 'td':
                # Convert td to th for header row
                new_th = soup.new_tag('th')
                new_th.string = cell.get_text()
                new_th['scope'] = 'col'
                # Copy any existing attributes
                for attr, value in cell.attrs.items():
                    new_th[attr] = value
                cell.replace_with(new_th)
            elif cell.name == 'th':
                # Add scope if missing
                if 'scope' not in cell.attrs:
                    cell['scope'] = 'col'

    # Process remaining rows - first cell as row header
    for row in rows[1:]:
        cells = row.find_all(['td', 'th'])
        if cells:
            first_cell = cells[0]
            if first_cell.name == 'td':
                # Convert first cell to th with row scope
                new_th = soup.new_tag('th')
                new_th.string = first_cell.get_text()
                new_th['scope'] = 'row'
                # Copy any existing attributes
                for attr, value in first_cell.attrs.items():
                    new_th[attr] = value
                first_cell.replace_with(new_th)

    # Return only the table part, not full HTML document
    return str(table)

# Example usage
if __name__ == "__main__":
    sample_html = """
    <table>
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
        <tr>
            <td>Jane</td>
            <td>30</td>
            <td>LA</td>
        </tr>
    </table>
    """
    formatted_html = add_wcag_styles(sample_html)
    print(formatted_html)