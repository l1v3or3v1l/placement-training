n = int(input())
a = list(map(int, input().split()))

# i, j = 0, 0
# while i < n and j < n:
#     if a[j] != 0:
#         a[i], a[j] = a[j], a[i]
#         i += 1
#     j += 1

i = 0
for j in range(n):
    if a[j] != 0:
        a[i] = a[j]
        i += 1

while i < n:
    a[i] = 0
    i += 1

print(a)