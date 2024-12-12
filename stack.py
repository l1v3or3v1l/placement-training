# peek = value of last added element
# top = index of last added element
# push = append
# pop = pop
# top = L[-1]

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

s = Stack()
s.push(1)
s.push(2)
s.push(3)
t = s.top()
print(t)
s.pop()
t = s.top()
print(t)
