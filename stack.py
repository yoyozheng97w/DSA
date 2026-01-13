"""
用 List 實作 Stack

Operations:
    isEmpty: 
        Checks if the stack is empty.
        O(1)
    Push: 
        Adds a new element on the stack.
        O(1)
    Pop: 
        Removes and returns the top element from the stack.
        O(1)
    Peek: 
        Returns the top (last) element on the stack.
        O(1)
    Size: 
        Finds the number of elements in the stack.
        O(n)
"""
class Stack:
    def __init__(self):
        self.stack = []

    # isEmpty
    def isEmpty(self):
        return len(self.stack) == 0
    
    # push
    def push(self, ele):
        self.stack.append(ele)
    
    # pop
    def pop(self):
        if self.isEmpty():
            return "stack is Empty!"
        else:
            return self.stack.pop()
    
    # peek
    def peek(self):
        if self.isEmpty():
            return "stack is Empty!"
        return self.stack[-1]
    
    # size
    def size(self):
        return len(self.stack)

# Create s stack
myStack = Stack()

myStack.push('A')
myStack.push(1)
print(myStack.stack)
print("pop:", myStack.pop())
print(myStack.stack)
print("peek:", myStack.peek())
print("isEmpty:", myStack.isEmpty())
print("size:", myStack.size())
