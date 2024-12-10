n = int(input())
c = n
l = 0

while n != 0:
    n //= 10
    l += 1

n = c
s = 0

while n != 0:
    r = n % 10
    s += r ** l
    n //= 10
    l -= 1
    
if s == c:
    print(f"{s} is a disarium number")
else:
    print(f"{s} is not a disarium number")