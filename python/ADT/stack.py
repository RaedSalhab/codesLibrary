# Completed implementation of a stack ADT

class Stack:
    """ Stack implementation using a Python list."""

    def __init__(self):
        """Create an empty stack"""
        self._items = []

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self._items) == 0

    def push(self, item):
        """Add item to the top of the stack."""
        self._items.append(item)

    def pop(self):
        """Return and remove the element at the top of the stack.
        Raise exception if the stack is empty
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._items.pop()

    def peek(self):
        """Return (but do not remove) the element at the top of the stack.
        Raise exception if the stack is empty
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._items[-1]

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._items)
    
    def size(self):
        """Return the number of elements in the stack."""
        return len(self._items)
    
    def __str__(self):
        """Return stack as string"""
        return str(self._items)