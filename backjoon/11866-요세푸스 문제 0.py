n, k = map(int, input().split())

arr = [i for i in range(1,n+1)]
result = []

index=0

while arr:
    index+=k-1
    index%=len(arr)
    result.append(arr.pop(index))


print(f"<{', '.join(map(str,result))}>")
