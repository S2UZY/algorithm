import heapq
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    M = int(input())
    ipt = []
    for _ in range(M//10+1):
        while len(ipt)<M:
            for i in map(int, input().split()):
                ipt.append(i)
    ans = []
    max_hq = []
    min_hq = []
        
    def put(n):
        if max_hq and n >= -max_hq[0]:
            heapq.heappush(min_hq,n)
        else:
            heapq.heappush(max_hq,-n)
        if len(max_hq)>len(min_hq) +2:
            heapq.heappush(min_hq,-heapq.heappop(max_hq))
        elif len(max_hq)<len(min_hq):
            heapq.heappush(max_hq,-heapq.heappop(min_hq))

    for i , val in enumerate(ipt):
        put(val)
        if i%2 == 0:
            ans.append(-max_hq[0])

    print((M+1)//2)
    for i in range(len(ans)//10+1):
        print(*ans[i*10:(i+1)*10])
