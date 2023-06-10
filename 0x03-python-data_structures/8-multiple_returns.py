def multiple_returns(sentence):
    """A function that returns a tuple with the length of a string
    and its first character"""

    string_length = len(sentence)
    if string_length == 0:
        first_char = "None"
    else:
        first_char = sentence[0]
    return string_length, first_char
