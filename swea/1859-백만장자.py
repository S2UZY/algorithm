T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    arr = list(map(int, input().split()))

    arr.reverse()
    anw = 0
    max_num = arr[0]

    for i in arr:
        if max_num > i:
            anw += max_num-i
        elif max_num < i:
            max_num = i
        
    print(f"#{test_case} {anw}")