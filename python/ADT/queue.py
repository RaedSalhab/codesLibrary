from turtle import st


class Queue():
    def __init__(self) -> None:
        self._items = []
        
    def is_empty(self):
        return self._items == []
    
    def enqueue(self, item):
        self._items.insert(0,item)
        
    def dequeue(self):
        return self._items.pop()
    
    def size(self):
        return len(self._items)
    
    def __str__(self) -> str:
        return str(self._items)
    