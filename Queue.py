
#Queues - FIFO 
#lookup O(n)
#enqueue O(1)
#dequeue O(1)
#peel O(1)
#printer, lines, reservations, etc
#not efficient to build from arrays because you'd have to keep shifting the indexes 


#queue 
class Queue: 
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0 

    def peek(self):
        return self.first.value
    
    def enqueue(self, value):
        tempNode = Node(value)
        if self.length == 0:
            self.first = tempNode
            self.last = tempNode
        else:
            self.last.next = tempNode
            self.last = tempNode
        self.length += 1

    def dequeue(self):
        if self.first == None:
            return None
        if self.first is self.last:
            this.last = None

        dequeueNode = self.first
        self.first = dequeueNode.next
        self.length -= 1
        return dequeueNode.value

myQ = Queue()
myQ.enqueue("1")
myQ.enqueue("2")
myQ.enqueue("3")
print(myQ.dequeue())
print(myQ.peek())
