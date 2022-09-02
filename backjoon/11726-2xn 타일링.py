import sys

sys.setrecursionlimit(10**6)
N = int(input())
cache = [0] * (N+1)

def f(n):
	if cache[n]:
		return cache[n]

	cache[n] = n if n<3 else (f(n-1) + f(n-2)) % 10007
	return cache[n]

print(f(N))