
# WCAG Table Formatter
Making table html formatting easier
=======
This project provides a Python tool for cleaning up HTML table code and applying WCAG (Web Content Accessibility Guidelines) styles to enhance accessibility. The tool identifies table elements and formats them by adding appropriate `<th>` tags and `scope` attributes.

## Features

- Parses HTML table code to identify elements.
- Cleans up the table structure.
- Applies WCAG-compliant styles to improve accessibility.

## Installation

To get started, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd wcag-table-formatter
pip install -r requirements.txt
```

## Usage

Run the program using the following command:

```bash
python src/main.py <input-html-file>
```

Replace `<input-html-file>` with the path to your HTML file containing the table you want to format.

## Testing

To run the unit tests for the formatter, navigate to the `tests` directory and execute:

```bash
python -m unittest test_formatter.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
>>>>>>> 38c0d3d (initial commit)
