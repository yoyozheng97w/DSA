"""
用 List 實作 Stack

Time Complexity:
    push: O(1)
    pop: O(1)
    peek: O(1)
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
