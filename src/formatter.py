def add_wcag_styles(html_table):
    from bs4 import BeautifulSoup

    # Parse the HTML table
    soup = BeautifulSoup(html_table, 'html.parser')
    table = soup.find('table')

    if not table:
        return html_table  # Return original if no table found

    # Add <th> tags and scope attributes
    for row in table.find_all('tr'):
        headers = row.find_all('th')
        if headers:
            for th in headers:
                th['scope'] = 'col'  # Set scope for column headers
        else:
            # If no <th> found, assume first cell is a header
            first_cell = row.find('td')
            if first_cell:
                new_th = soup.new_tag('th', scope='row')
                new_th.string = first_cell.string
                first_cell.insert_before(new_th)
                first_cell.unwrap()  # Remove the original <td>

    return str(soup)  # Return the modified HTML as a string

# Example usage
if __name__ == "__main__":
    sample_html = """
    <table>
        <tr>
            <td>Header 1</td>
            <td>Header 2</td>
        </tr>
        <tr>
            <td>Row 1, Col 1</td>
            <td>Row 1, Col 2</td>
        </tr>
    </table>
    """
    formatted_html = add_wcag_styles(sample_html)
    print(formatted_html)