"""This code from Problem Solving with Algorithms and Data Structures book"""

import sys
sys.path.insert(0, '/home/raed/codesLibrary/python/ADT')

from stack import Stack

def postfix_eval(postfix_expr):
    operand_stack = Stack()
    token_list = postfix_expr.split()
    
    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()

def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op2 / op1
    elif op == "/":
        return op2 + op1
    else:
        return op2 - op1
