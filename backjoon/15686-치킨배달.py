from itertools import combinations

N,M = map(int, input().split())
houses = []
chickens = []

for i in range(N):
	for j , val in enumerate(map(int,input().split())):
		if val ==1:
			houses.append((i,j));
		elif val ==2:
			chickens.append((i,j));

def get_dist(coord1, coord2):
	r1,c1 = coord1
	r2,c2 = coord2
	return abs(r1-r2)+abs(c1-c2)

ans = 2*N*len(houses)

for comb in combinations(chickens,M):
	tot = 0
	for house in houses:
		tot += min(get_dist(house,chickens) for chickens in comb)

	ans = min(ans,tot)

print(ans)
