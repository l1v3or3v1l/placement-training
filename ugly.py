def isPrime(n):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			return False
	return True


n = int(input())

flag = False

if n in [2, 3, 5]:
	flag = True

for i in range(6, n + 1):
	if n % i == 0 and isPrime(i):
		flag = True
		break

if flag:
	print("yuck ugly")
else:
	print("wow beautiful")
