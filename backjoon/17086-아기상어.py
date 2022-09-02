n, m = map(int,input().split())
arr = []
x = [-1,-1,-1,0,0,1,1,1]
y = [-1,0,1,1,-1,-1,0,1]
q = []

for i in range(n):
	arr.append(list(map(int,input().split())))

for i in range(n):
	for j in range(m):
		if arr[i][j] == 1:
			for k in range(8):
				dy = i + y[k]
				dx = j + x[k]
				if 0>dy or dy>=n or 0>dx or dx>=m:
					continue
				else:
					print("dy,dx : ",dy,dx)
					arr[dy][dx] = 2
					for g in arr:
						print(g)
					print("--------------")

for i in arr:
	print(i)

		