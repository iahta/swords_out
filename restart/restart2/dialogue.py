import textwrap
import os

def print_wrapped(text):
    # Get the width of the terminal dynamically
        width = os.get_terminal_size().columns
    # Wrap the text
        wrapped_text = textwrap.fill(text, width)
    # Print the wrapped text
        print(wrapped_text)


        