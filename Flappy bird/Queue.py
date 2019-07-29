class Queue:
    def __init__(self):
        self.data = [None] * 10
        self.size = 0
        self.front = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def enqueue(self,num):
        if self.size == len(self.data):
            self.resize(len(self.data)*2)
        aval = (self.size + self.front) % len(self.data)
        self.data[aval] = num
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Invalid")
        val = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front+1) % len(self.data)
        self.size -= 1
        return val
        
        
    def first(self):
        if self.is_empty():
            raise IndexError("Invalid")
        val = self.data[self.front]
        return val

    def resize(self,capacity):
        new_data = [None] * capacity
        cur = self.front
        for i in range(self.size):
            new_data[i] = self.data[cur]
            cur = (cur+1) % len(self.data)
        self.front = 0   
        self.data = new_data

    def __iter__(self):
        for i in self.data:
            yield i

    def __getitem__(self,ind):
        return self.data[ind]

    def __setitem__(self,ind,val):
        self.data[ind] = val
 

    

