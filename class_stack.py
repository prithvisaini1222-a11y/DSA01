class Stack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
#time complexity-O(1). Because from push the element adds at the end of the stack so the time complexity is O(1).
        print(x, "pushed to stack")

    def pop(self):
#time complexity-O(1).Because when we removed element it removes from the last so the time complexity is O(1).

        if len(self.stack) == 0:
            print("Stack Underflow")
        else:
            print(self.stack.pop(), "popped from stack")

    def peek(self):
#time complexity -O(1).Because when we peek any element it returns the topest value present in the stack.
        if len(self.stack) == 0:
            print("Stack is Empty")
        else:
            print("Top element:", self.stack[-1])
#time complexity-O(1).

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.peek()
s.pop()
s.peek()
s.push(22)
s.push(14)