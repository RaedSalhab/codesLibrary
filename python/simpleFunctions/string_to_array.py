import imp
from string_length import string_length

def string_to_array(string):
    """
    string_to_array function convert a string to array of characters
    """
    new_list = []
    # first solution
    i = 0
    while i < string_length(string):
        new_list.append(string[i])
        i += 1

    # for loop comprehension
    # [new_list.append(ch) for ch in string]
    return new_list