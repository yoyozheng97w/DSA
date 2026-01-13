"""
用 List 實作 Queue

Operations:
    isEmpty: 
        Checks if the queue is empty.
        O(1)
    Enqueue: 
        Adds a new element to the queue.
        O(1)
    Dequeue: 
        Removes and returns the first (front) element from the queue.
        O(1)
    Peek: 
        Returns the first element on the queue.
        O(1)
    Size: 
        Finds the number of elements in the queue.
        O(n)
"""
class queue:
    def __init__(self):
        self.queue = []

    # isEmpty
    def isEmpty(self):
        return len(self.queue) == 0
    
    # enqueue
    def enqueue(self, ele):
        self.queue.append(ele)
    
    # dequeue
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty!"
        else:
            return self.queue.pop(0)
    
    # peek
    def peek(self):
        if self.isEmpty():
            return "queue is Empty!"
        return self.queue[0]
    
    # size
    def size(self):
        return len(self.queue)

# Create s queue
myQueue = queue()

myQueue.enqueue('A')
myQueue.enqueue(1)
print(myQueue.queue)
print("dequeue:", myQueue.dequeue())
print(myQueue.queue)
print("peek:", myQueue.peek())
print("isEmpty:", myQueue.isEmpty())
print("size:", myQueue.size())
