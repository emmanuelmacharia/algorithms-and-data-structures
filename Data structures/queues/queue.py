class Queue:
    def __init__(self, maxSize):
        self.queue = []
        self.rear = - 1
        self.front = 0
        self.size = 0

        
    def isFull(self): 
        if self.size == self.maxSize: #if self.rear == self.maxSize  - 1
            return True
    
    def isEmpty(self):
        if self.size == 0:
            return True
        #  if len(self.queue) == 0: # if  self.rear < self.front
        #     return True

    def peek(self):
        return self.queue[self.front]
        
    def enque(self, data):
        if not self.isFull():
           return  self.queue.append(data)
        
    def deque(self):
        if not self.isEmpty():
          return self.queue.pop(self.front)



myQueue = Queue(10)