from string_length import string_length

def string_reverse(string):
    """
    string_reverse function return a string in reverse order
    """
    index = string_length(string) - 1
    reversed_string = ""
    while index >= 0:
        reversed_string += string[index]
        index -= 1

    return reversed_string