# n = int(input())
# arr = [i for i in range(1,n+1)]

# while len(arr) > 1:
#         arr.pop(0)
#         arr.append(arr.pop(0))

# print(arr[0])

from collections import deque

n = int(input())
dq = deque()

for i in range(1,n+1):
    dq.append(i)

while len(dq)>1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])