from ADT.stack import Stack

def rev_string(my_string):
    """Reverse string by using stack abstract data type"""
    ch_stack = Stack()
    rev_str = ''
    for ch in my_string:
        ch_stack.push(ch)

    while not ch_stack.is_empty():
        rev_str += ch_stack.pop() 

    return rev_str

