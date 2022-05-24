N,L = map(int ,input().split())
data = list(map(int ,input().split()))
data.sort()

curFix = 0
cnt = 0

for x in data:
	if x >= curFix:
		cnt +=1
		curFix = x+L

print(cnt)