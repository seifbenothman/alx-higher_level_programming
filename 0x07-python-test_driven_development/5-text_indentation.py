#!/usr/bin/python3
"""
Print a text with 2 new lines after each of these characters: ., ? and :
    """


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text:
        print('#')
        return

    new_text = ""
    newline = True
    for char in text:
        if char in [':', '.', '?']:
            new_text += char + '\n\n'
            newline = True
        else:
            if newline and char == ' ':
                continue
            new_text += char
            newline = False

    print(new_text, end='')


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
