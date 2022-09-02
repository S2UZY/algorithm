import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
chk = [False] *(N+1)
adj = [[False]*(N+1)  for _ in range(N+1)]

for _ in range(M):
	s, e = map(int, input().split())
	adj[s][e] = True
	adj[e][s] = True

ans = 0

def dfs(i):
	for j in range(1,N+1):
		if adj[i][j] and not chk[j]:
			chk[j] = True
			dfs(j)

for i in range(1,N+1):
	if not chk[i]:
		ans += 1
		chk[i] = True
		dfs(i)

print(ans)