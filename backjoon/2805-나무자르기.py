n, m = map(int, input().split())
tree = list(map(int,input().split()))

#절단기 길이
left = 0
right = max(tree)
mid = (left+right)//2

while left <= right:
	h = 0
	for i in tree:
		if i-mid >=0:
			h += i-mid
	
	if h == m:
		break
	elif h<m:
		right = mid - 1 
	else:
		left = mid+1

	mid = (left+right)//2

print(mid)