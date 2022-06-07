def string_repeat(string, repeats = 2, separator = ""):

    """string_repeat function used for repeat a string with number of repeats and 
    separator between strings
    """
    final_string = string
    while repeats > 1:
        final_string +=  separator + string
        repeats -= 1

    return final_string


