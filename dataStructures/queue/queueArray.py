class queueArray:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) ==0
    
    # isert data to the queue
    def enqueue(self,e):
        self._data.append(e)
    
    def dequeue(self):
        if self.isempty():
            print("Empty Queue")
            return
        return self._data.pop(0)
    
    def first(self):
        if self.isempty():
            print('Empty queue')
            return
        return self._data[0]

q = queueArray()
q.enqueue(3)
q.enqueue(7)
q.enqueue(5)
q.enqueue(6)
q.enqueue(8)

print(q._data)

print(q.dequeue())

print(q.first())