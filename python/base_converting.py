from ADT.stack import Stack

def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()
    new_string = ""
    if dec_number == 0:
        new_string = "0"
    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    while not rem_stack.is_empty():
        new_string += digits[rem_stack.pop()]

    return new_string