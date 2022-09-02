import sys

input = sys.stdin.readline
i = 0

while True:
	i +=1
	l,p,v = map(int, input().split())
	if l ==0 and p==0 and v==0:
		break
	
	print(f'Case {i}: {v//p*l+min(v%p,l)}')