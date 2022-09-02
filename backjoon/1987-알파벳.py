from collections import deque

dx = (0,0,-1,1)
dy = (-1,1,0,0)

N, M = map(int,input().split())
board = [list(input()) for _ in range(N)]
chk = [['' for _ in range(M)] for _ in range(N)]
ans = 0

def is_valid_coord(y,x):
	return 0<=y<N and 0<=x<M

q = deque()
chk[0][0] = board[0][0]
q.append((0,0,board[0][0]))

while q:
	y,x,s = q.popleft();
	ans = max(ans,len(s))

	for i in range(4):
		nx = x+dx[i]
		ny = y+dy[i]

		if is_valid_coord(ny,nx) and board[ny][nx] not in s:
			ns = s + board[ny][nx]
			if ns not in chk[ny][nx]:
				chk[ny][nx] = ns
				q.append((ny,nx,ns))

print(ans)