a = [23, 46, 2, 12, 6]

n = len(a)

for i in range(n):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)