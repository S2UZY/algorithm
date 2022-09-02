data = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
visited = []
stack = []

visited.append("ICN")

while True:
	s = visited[-1];

	for i in range(0,len(data)):
		if data[i][0]==s and data[i][1]!='v':
			stack.append([data[i][1],i])

	if stack:
		stack.sort()
		visited.append(stack[0][0])
		data[stack[0][1]][1]='v'
		stack.clear()
	else:
		break

print(visited)