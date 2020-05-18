#!/usr/bin/python3
def roman_to_int(roman_string):
    arab = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    values = {}
    counter = 0
    product = 0
    for letter in roman_string:
        if values.get(letter):
            values[letter] = values[letter] + arab[letter]
        else:
            values[letter] = arab[letter]
    for number in reversed(list(values.values())):
        if product > number:
            product = product - number
        else:
            product = product + number
    return product
