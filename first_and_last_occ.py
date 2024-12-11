a = list(map(int, input().split()))
l = 0
r = len(a) - 1
f = -1
k = int(input())

while l <= r:
	mid = (l + r) // 2
	if a[mid] == k:
		f = mid
		r = mid - 1
	elif a[mid] < k:
		l = mid + 1
	else:
		r = mid - 1

print(f"First occ: {f}")

l = 0
r = len(a) - 1
la = -1

while l <= r:
	mid = (l + r) // 2
	if a[mid] == k:
		la = mid
		l = mid + 1
	elif a[mid] < k:
		l = mid + 1
	else:
		r = mid - 1


print(f"Last occ: {la}")