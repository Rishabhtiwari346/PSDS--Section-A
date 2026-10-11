class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(data, "pushed")
        
    def pop(self):
        if self.top is None:
            print("stack is empty")
        else:
            print(self.top.data, "popped")
            self.top = self.top.next
            
    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()

s = Stack()
s.push(5)
s.push(10)
s.push(15)
s.push(20)
s.push(25)

print("Stack:")
s.display()
s.pop()
print("After pop : ")
s.display() 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(data, "enqueued")
        
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print(self.front.data, "dequeued")
            self.front = self.front.next
        if self.front is None:
            self.rear = None
            
    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end = " ")
            temp = temp.next
        print()

q = Queue()
q.enqueue(15)
q.enqueue(25)
q.enqueue(35)

print("Queue is:")
q.display()
q.dequeue()
print("After dequeue:")
q.display()