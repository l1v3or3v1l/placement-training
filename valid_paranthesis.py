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

s = input()
stack = Stack()
for c in s:
    if c in "{[(":
        stack.push(c)
    else:
        top = stack.top()
        if top == '{' and c == '}':
            stack.pop()
        if top == '(' and c == ')':
            stack.pop()
        if top == '[' and c == ']':
            stack.pop()
if stack.isempty():
    print(True)
else:
    print(False)
