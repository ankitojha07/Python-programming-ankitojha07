class _Node :
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        self._element = element
        self._next = next

class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def isempty(self):
        return self._size == 0

    def addlast(self,e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def search(self, key):
        p = self._head
        index = 1
        while p:
            if p._element == key:
                return index
            p = p._next
            index+=1
        return -1

    # insertion starts here
    def insertfirst(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._head = newest
            self._tail = newest
        else : 
            newest._next = self._head
            self._head = newest
        self._size +=1

    def insertanywhere(self,e,pos):
        newest = _Node(e, None)
        p = self._head
        i =0
        while i < pos-1:
            p = p._next
            i += 1
        newest._next = p._next
        p._next = newest
        self._size +=1



    def display(self):
        print()
        p = self._head
        while p:
            if p._next!=None:
                print(p._element,end=' --> ')
            
            else:
                print(p._element)
            p = p._next   
        print()

L = LinkedList()
L.addlast(2)
L.addlast(4)
L.addlast(6)
L.addlast(3)
L.addlast(9)

print('Printing Linked List : ')
L.display()

print('Size : ', len(L))

# print('Element found at : ',L.search(4))
print()
print()
print("--------------------- After insertion at first ------------------------------------- ")
L.insertfirst(90)
print('Printing Linked List : ')
L.display()
print('Size : ', len(L))

#insert at anywhere
print()
print()
print("--------------------- After insertion at Position ------------------------------------- ")
L.insertanywhere(94,4)
print('Printing Linked List : ')
L.display()
print('Size : ', len(L))
