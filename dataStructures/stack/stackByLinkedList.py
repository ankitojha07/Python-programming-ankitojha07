class _Node:
    __slots__ = '_element','_next'

    def __init__(self,element,next):
        self._element = element
        self._next = next

class StacksLinked:
    def __init__(self):
        self._top = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0
    