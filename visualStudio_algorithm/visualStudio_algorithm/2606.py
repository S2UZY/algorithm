n = int(input())
case = int(input())
graph = [[] for _ in range(n+1)]
queue = []
visited = []
result = 0

for i in range(case):
	s,e = map(int,input().split())
	graph[s].append(e)
	graph[e].append(s)

queue.extend(graph[1])
visited.append(1)

while queue:
	node = queue.pop()
	if node in visited:
		continue
	else:
		result+=1
		visited.append(node)
		queue.extend(graph[node])

print(result)