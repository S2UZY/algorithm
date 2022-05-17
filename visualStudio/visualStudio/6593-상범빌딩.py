dl = [-1,1,0,0,0,0]
dr = [0,0,-1,1,0,0]
dc = [0,0,0,0,-1,1]
L,R,C = 0,0,0
result = []

def bfs(graph, sl, sr, sc):
	visited = [[[0] * C for _ in range(R)] for _ in range(L)]
	visited[sl][sr][sc] = 1
	q = []

	q.append((sl,sr,sc))
	while q:
		l, r, c = q.pop(0)
		for i in range(6):
			nl = l +dl[i]
			nr = r +dr[i]
			nc = c +dc[i]

			if not (0<=nl <L and 0<= nr < R and 0<= nc < C):
				continue
			if visited[nl][nr][nc] or b[nl][nr][nc] == '#':
				continue
			if b[nl][nr][nc] == 'E':
				result.append(("Escaped in {} minute(s).".format(visited[l][r][c])))
				return

			visited[nl][nr][nc] = visited[l][r][c]+1
			q.append((nl,nr,nc))
	result.append("Trapped!")


while True:
	L,R,C = map(int,input().split())
	
	if L == 0 and R==0 and C==0:
		break
	
	b = []
	sl , sr, sc = -1,-1,-1
	for i in range(0,L):
		b_l = []
		for j in range(0,R):
			b_l.append(list(input()))
			for k in range(0,C):
				if b_l[j][k] == 'S':
					sl , sr, sc = i,j,k
		b.append(b_l)
		input()
	bfs(b,sl,sr,sc)

for i in result:
	print(i)