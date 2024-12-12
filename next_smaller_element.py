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
    
a = list(map(int, input().split()))
stack = Stack()
stack.push(-1)
ans = [0] * len(a)
for i in range(len(a) - 1, -1, -1):
    while stack.top() != -1 and stack.top() > a[i]:
        stack.pop()
    ans[i] = stack.top()
    stack.push(a[i])
print(ans)