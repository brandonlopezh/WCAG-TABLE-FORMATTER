import unittest
from src.formatter import format_table

class TestTableFormatter(unittest.TestCase):

    def test_format_table_with_simple_html(self):
        input_html = "<table><tr><td>Data 1</td><td>Data 2</td></tr></table>"
        expected_output = "<table><tr><th scope='row'>Data 1</th><th scope='row'>Data 2</th></tr></table>"
        self.assertEqual(format_table(input_html), expected_output)

    def test_format_table_with_headers(self):
        input_html = "<table><tr><th>Header 1</th><th>Header 2</th></tr><tr><td>Data 1</td><td>Data 2</td></tr></table>"
        expected_output = "<table><tr><th scope='col'>Header 1</th><th scope='col'>Header 2</th></tr><tr><td>Data 1</td><td>Data 2</td></tr></table>"
        self.assertEqual(format_table(input_html), expected_output)

    def test_format_table_with_multiple_rows(self):
        input_html = "<table><tr><td>Row 1 Col 1</td><td>Row 1 Col 2</td></tr><tr><td>Row 2 Col 1</td><td>Row 2 Col 2</td></tr></table>"
        expected_output = "<table><tr><th scope='row'>Row 1 Col 1</th><th scope='row'>Row 1 Col 2</th></tr><tr><th scope='row'>Row 2 Col 1</th><th scope='row'>Row 2 Col 2</th></tr></table>"
        self.assertEqual(format_table(input_html), expected_output)

    def test_format_table_with_no_rows(self):
        input_html = "<table></table>"
        expected_output = "<table></table>"
        self.assertEqual(format_table(input_html), expected_output)

if __name__ == '__main__':
    unittest.main()