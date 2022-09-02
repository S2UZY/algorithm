import sys

input = sys.stdin.readline
data = []
for _ in range(int(input())):
	start, end = map(int,input().split())
	data.append((end,start))

data.sort()
curTime = 0
cnt = 0

for i in data:
	end, start = i
	if curTime <= start:
		cnt +=1
		curTime = end

print(cnt)

