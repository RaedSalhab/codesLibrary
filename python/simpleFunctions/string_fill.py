def string_fill(a_string: str, length: int, space: str):
    spaces = length - len(a_string)
    new_string = spaces * space + a_string
    return new_string