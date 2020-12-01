#stacks and queues and linear data structures 
#control over what the user can do 

#stacks - LIFO 
#lookup O(n)
#pop O(1)
#push O(1)
#peek O(1)
#need to know latest added value 
#memory design in most languages 
#browser history 
#built with arrays or Linked Lists 
#array faster acces of memory since they are next to each other in memory 
#linked list more flexiblity with adding to memory 

#build it with linkedlist 
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top

    def push(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
            self.length += 1
        else:
            currTop = self.top
            self.top = newNode
            self.top.next = currTop
            self.length += 1
        return self

    def pop(self):
        if self.top is None:
            return None
        if self.top is self.bottom:
            self.bottom = None

        currTop = self.top
        newTop = self.top.next
        self.top = newTop
        self.length -= 1
        return currTop

    def isEmpty(self):
        if self.length == 0:
            return True
        return False

myStack =  Stack()
myStack.push('1')
myStack.push('2')
myStack.push('3')
myStack.pop()
myStack.pop()
myStack.pop()
print(myStack.top)