import sys
from formatter import add_wcag_styles  # Import your function

def get_user_input():
    print("Paste your HTML table below (press Ctrl+D on Mac/Linux or Ctrl+Z+Enter on Windows when done):")
    print("-" * 50)
    lines = []
    try:
        while True:
            line = input()
            lines.append(line)
    except EOFError:
        pass
    
    return '\n'.join(lines)

def main():
    try:
        html_content = get_user_input()
        
        if not html_content.strip():
            print("No input provided. Exiting.")
            return
        
        print("\nProcessing...")
        formatted_html = add_wcag_styles(html_content)  # Use your function
        
        print("\n" + "="*50)
        print("WCAG-FORMATTED TABLE:")
        print("="*50)
        print(formatted_html)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()