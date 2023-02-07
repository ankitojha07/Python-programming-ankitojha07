class _Node:
    __slots__ = ('_element', '_next')

    def __init__(self,element,next):
        self._element = element
        self._next = next

class DequeLinked:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return len(self._size)
    
    def isempty(self):
        return self._size == 0

    def addfirst(self,e):
        newest = _Node(e, None)
        if self.isempty():
            self._front = newest
            self._rear = newest
        
        else:
            newest._next = self._front
            self._front = newest
        self._size += 1


    def addlast(self,e):
        newest = _Node(e, None)
        if self.isempty():
            self._front = newest
        
        else:
            self._rear._next = newest
        self._rear = newest
        self._size += 1

    def removefirst(self):
        if self.isempty():
            print('Empty dequeue')
            return
        v = self._front._element
        self._front = self._front._next
        self._size -= 1
        if self.isempty():
            self._rear = None
        return v

    def removelast(self):
        if self.isempty():
            print('Empty dequeue')
            return
        
        p = self._front
        i = 1

        while i<len(self)-1:
            p = p._next
            i += 1
        self._rear = p
        p = p._next
        v = p._element
        self._rear._next = None
        self._size -= 1
        return v

    def first(self):
        if self.isempty():
            print('Empty dequeue')
            return
        return self._front._element

    def last(self):
        if self.isempty():
            print('Empty dequeue')
            return
        return self._rear._element


    def displey(self):
        p = self._front
        if self.isempty():
            print('Empty dequeue')
            return
        while p:
            print(p._element, end='  --> ')
            p = p._next
        print()

d = DequeLinked()
d.addfirst(3)
d.addfirst(4)
d.addfirst(6)
d.addfirst(7)
d.addfirst(8)

d.displey()
    