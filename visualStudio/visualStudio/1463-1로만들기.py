n = int(input())
cache = [-1]*(n+1)

for i in range(n+1):
	if i==1:
		cache[i] = 0
		continue
	elif 1< i <=3:
		cache[i] = 1
		continue
	
	temp =[]
	if i%3==0:
		temp.append(cache[i//3]+1)
	if i%2==0:
		temp.append(cache[i//2]+1)

	temp.append(cache[i-1]+1)

	cache[i] = min(temp)

print(cache[n])