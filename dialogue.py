import textwrap
import os
import time

def print_wrapped(text):
    # Get the width of the terminal dynamically
        width = os.get_terminal_size().columns
    # Wrap the text
        wrapped_text = textwrap.fill(text, width)
    # Print the wrapped text
        time.sleep(1)
        print(wrapped_text)


def print_king(text):
    # Get the width of the terminal dynamically
        width = os.get_terminal_size().columns
    # Wrap the text
        wrapped_text = textwrap.fill(text, width)
    # Print the wrapped text
        time.sleep(1)
        print(f"\033[32m{wrapped_text}\033[0m")




        

"""other wrapped functions with the text editied. maybe with evidence to determine,
if inventory or if it had been found """


