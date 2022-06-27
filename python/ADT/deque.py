"""Completed implementaion of a deque ADT """

class Deque:
    def __init__(self) -> None:
        self._items = []
        
    def is_empty(self):
        return self._items == []
    
    def add_front(self, item):
        self._items.append(item)
        
    def add_rear(self, item):
        self._items.insert(0, item)
        
    def remove_front(self):
        return self._items.pop()
        
    def remove_rear(self):
        return self._items.pop(0)
        
    def size(self):
        return len(self._items)
    
    def __str__(self) -> str:
        return str(self._items)