l = list(map(int, input().split()))

c_sum = 0
m_sum = -999

for i in range(0, len(l)):
	c_sum += l[i]
	
	if c_sum > m_sum:
		m_sum = c_sum
	
	if c_sum < 0:
		c_sum = 0

print(m_sum)