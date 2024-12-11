s = input()
t = input()

counter = {}

for c in s:
	if c in counter:
		counter[c] += 1
	else:
		counter[c] = 1

flag = True

for c in t:
	if c in counter:
		counter[c] -= 1
		if counter[c] == 0:
			del counter[c]
	else:
		flag = False

if len(counter) != 0:
	flag = False

if flag:
	print("is anagram")
else:
	print("not anagram")