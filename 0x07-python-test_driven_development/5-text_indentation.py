#!/usr/bin/python3
"""
  4-text_indentation module.
  Indent strings
  Functions:
    text_indentation(text)
"""


def text_indentation(text):
    """
        Prints a text with 2 new lines after
        each of these characters: ., ? and :
        Args:
          text: text to indent
        Raises:
          TypeError: text must be an string
    """
    fixed = []
    idx = 0
    lim = ('.', '?', ':')

    if type(text) is not str:
        raise TypeError("text must be a string")
    for idx in range(len(text)):
        if text[idx] in lim:
            fixed.append("\n")
            fixed.append("\n")
            continue
        if text[idx] == " ":
            if text[idx - 1] in lim or text[idx - 1] == " ":
                continue
        fixed.append(text[idx])
    fixed = ''.join(fixed)
    print(fixed)
