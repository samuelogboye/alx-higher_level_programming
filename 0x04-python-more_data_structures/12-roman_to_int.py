#!/usr/bin/python3
def roman_to_int(roman_string):
    """a function def roman_to_int: converts a Roman numeral to an integer"""
    if not roman_string or type(roman_string) != str:
        return 0
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    results = 0
    prev_value = 0
    for char in reversed(roman_string):
        char = char.upper()
        if char not in romans:
            return 0
        value = romans[char]
        if value >= prev_value:
            results += value
        else:
            results -= value

        prev_value = value

    return results
