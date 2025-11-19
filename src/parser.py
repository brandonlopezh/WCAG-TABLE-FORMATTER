def parse_html_table(html):
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')

    if not table:
        raise ValueError("No table found in the provided HTML.")

    headers = []
    rows = []

    for row in table.find_all('tr'):
        cells = row.find_all(['td', 'th'])
        if row.find('th'):
            headers.append([cell.get_text(strip=True) for cell in cells])
        else:
            rows.append([cell.get_text(strip=True) for cell in cells])

    return headers, rows

def add_wcag_attributes(headers, rows):
    formatted_rows = []
    for i, header in enumerate(headers):
        formatted_row = []
        for cell in header:
            formatted_row.append(f'<th scope="col">{cell}</th>')
        formatted_rows.append(formatted_row)

    for row in rows:
        formatted_row = []
        for cell in row:
            formatted_row.append(f'<td>{cell}</td>')
        formatted_rows.append(formatted_row)

    return formatted_rows

def format_table(headers, rows):
    formatted_rows = add_wcag_attributes(headers, rows)
    table_html = '<table>\n'
    
    for row in formatted_rows:
        table_html += '  <tr>\n'
        for cell in row:
            table_html += f'    {cell}\n'
        table_html += '  </tr>\n'
    
    table_html += '</table>'
    return table_html

def clean_and_format_table(html):
    headers, rows = parse_html_table(html)
    return format_table(headers, rows)