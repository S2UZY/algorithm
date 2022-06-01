import sys

input = sys.stdin.readline
N,M,K =  map(int, input().split())
board = [[0]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = (0,0,-1,1)
dy = (-1,1,0,0)

ans = 0

for i in range(K):
	r,c = map(int,input().split())
	board[r-1][c-1] = 1


def is_valid_coord(y,x):
	return 0<= y <N and 0<= x < M


for y in range(N):
	for x in range(M):
		if board[y][x] == 1 and not visited[y][x]:
			q = []
			q.append((y,x))
			size = 0
			while q:
				cy, cx = q.pop()
				visited[cy][cx] =True
				size += 1
				
				for _	in range(4):
					my = cy+dy[_]
					mx = cx + dx[_]

					if is_valid_coord(my,mx) and board[my][mx]==1 and not visited[my][mx]:
						q.append((my,mx))
						visited[my][mx] =True
						

			ans = max(ans,size)
						

print(ans)