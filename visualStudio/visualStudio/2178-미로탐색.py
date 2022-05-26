from collections import deque

nx = (0,0,-1,1)
ny = (-1,1,0,0)

N, M = map(int,input().split())
adj = []


for _ in range(N):
	temp = list(map(int,input()))
	adj.append(temp)

def check(y,x):
	return 0<=y<N and 0<=x<M

def BFS(sy,sx):
	q = deque()
	d = 1
	q.append((sy,sx,d))
	

	while q:
		y, x, d = q.popleft();
		if y == N-1 and x==M-1:
			return d

		if adj[y][x]==1:
			adj[y][x] = 0

			for i in range(4):
				cx = x+nx[i]
				cy = y+ny[i]
				cd = d+1
				if check(cy,cx):
					if adj[cy][cx]:
						q.append((cy,cx,cd))


print(BFS(0,0))