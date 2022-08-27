n = int(input())
a = list(map(int, input().split()))
nge = [ -1 for i in range(n)]
stk = []

for i in range(n):
	while stk and a[stk[-1]] < a[i]:
		nge[stk[-1]] = a[i]
		stk.pop(-1)

	stk.append(i)

print(' '.join(map(str,nge)))