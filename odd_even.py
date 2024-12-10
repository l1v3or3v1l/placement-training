n = int(input())
a = list(map(int, input().split()))
d = int(input())
x = int(input())

mod = d % 2
c = 0
for i in a:
    if i % 2 != mod:
        c += 1
print(c * x)