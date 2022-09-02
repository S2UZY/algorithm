n,m,k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
result = 0

for i in range(k):
	r,c = map(int, input().split())
	graph[r-1][c-1] = 1

for i in range(n):
	for j in range(m):
		if graph[i][j] == 1:
			queue = []
			queue.append([i,j])
			count = 0

			while queue:
				x,y = queue.pop()
				graph[x][y]=0
				count +=1

				for k in range(4):
					indexX = x+dx[k]
					indexY = y+dy[k]
					if indexX >= n or indexX < 0 or indexY < 0 or indexY>=m:
						continue
					elif graph[indexX][indexY] == 1:
						queue.append([indexX,indexY])
						graph[indexX][indexY]=0

				result = max(result, count)


print(result)