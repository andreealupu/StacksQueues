#array for stacks: 
class Stack2:
    def __init__(self):
        self.array = []

    def push(self,value):
        self.array.append(value)

    def peek(self):
        if len(self.array) > 0:
            return self.array[-1]
        return None
    
    def pop(self):
        if len(self.array) > 0:
            return self.array.pop()
            

myStack =  Stack2()
myStack.push('1')
myStack.push('2')
myStack.push('3')
myStack.pop()
print(myStack.array[1])