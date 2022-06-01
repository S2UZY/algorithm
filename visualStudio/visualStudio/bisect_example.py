from bisect import bisect_left, bisect_right


a = [2,3,4,5,5,5,6,6]
l = bisect_left(a,6)#스스로 정렬 안시킴 쭉 보다가 목표값보다 큰거 있으면 바로 출력
r = bisect_right(a,6) #목표값보다 큰거 없으면 LEN 반환

print(l,r)