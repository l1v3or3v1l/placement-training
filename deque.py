from collections import deque

# Initialise
dq = deque()
print(dq)

# Declare
dq = deque([1, 2, 3])
print(dq)

# Add values
dq.append(4)
print(dq)
dq.appendleft(6)
print(dq)

# Remove Values
dq.pop()
print(dq)
dq.popleft()
print(dq)
