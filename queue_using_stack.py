class Stack:
    def __init__(self):
        self.L = []

    def push(self, e):
        self.L.append(e)

    def pop(self):
        self.L.pop()

    def top(self):
        return self.L[-1]
    
    def isempty(self):
        if not self.L:
            return True
        return False

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def add(self, data):
        self.s1.push(data)

    def display(self):
        while not self.s1.isempty():
            self.s2.push(self.s1.top())
            self.s1.pop()
        while not self.s2.isempty():
            print(self.s2.top())
            self.s1.push(self.s2.top())
            self.s2.pop()

q = Queue()
q.add(1)
q.add(2)
q.add(3)
q.add(4)

q.display()