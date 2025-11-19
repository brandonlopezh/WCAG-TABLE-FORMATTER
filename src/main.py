def main():
    import sys
    from parser import parse_html_table
    from formatter import format_table

    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_html_file>")
        sys.exit(1)

    input_file_path = sys.argv[1]

    try:
        with open(input_file_path, 'r') as file:
            html_content = file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_file_path}' not found.")
        sys.exit(1)

    parsed_table = parse_html_table(html_content)
    formatted_table = format_table(parsed_table)

    print(formatted_table)

if __name__ == "__main__":
    main()