a = [25, 36, 12, 6, 2]

n = len(a)

for i in range(n):
    mini = i
    for j in range(i + 1, n):
        if a[j] < a[mini]:
            mini = j
    a[mini], a[i] = a[i], a[mini]

print(a)