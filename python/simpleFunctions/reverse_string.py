import sys
sys.path.insert(1, '/home/raed/codesLibrary/python/ADT')
from stack import Stack

def rev_string(my_string):
    ch_stack = Stack()
    rev_str = ''
    for ch in my_string:
        ch_stack.push(ch)

    while not ch_stack.is_empty():
        rev_str += ch_stack.pop() 

    return rev_str

print(rev_string("Raed Salhab"))