#나이트 이동거리 횟수 아는것이 포인트
#거리구하는건 BFS 
import sys
from collections import deque

input = sys.stdin.readline
testcase = int(input())

dx = (-2, -2, 2, 2, 1, 1,-1,-1)
dy = (1, -1, -1, 1, 2, -2, 2, -2)

def is_valid_coord(y,x,n):
	return 0<=y<n and 0<=x<n

for _ in range(testcase):
	n = int(input())
	sy, sx = map(int,input().split())
	ey, ex = map(int,input().split())
	q = deque()
	visited = [[False]*n for _ in range(n)]

	q.append((sy,sx,0))
	visited[sy][sx] = True
	
	while q:
		y,x,d = q.popleft()
		if y == ey and x==ex:
			print(d)
			break;

		for k in range(8):
			ny = y + dy[k]
			nx = x + dx[k]
			if is_valid_coord(ny,nx,n) and not visited[ny][nx]:
				q.append((ny,nx,d+1))
				visited[ny][nx] = True

