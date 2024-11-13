for test_case in range(1,11):
    length = int(input())
    arr = list(map(int, input().split()))
    ans = 0 

    for i in range(2,len(arr)-2):
        cur_ans = arr[i]

        for j in range(i-2,i+3):
            if j == i : continue
            if cur_ans > arr[i]-arr[j]:
                cur_ans = arr[i]-arr[j]
        if cur_ans > 0:
            ans += cur_ans
    print(f"#{test_case} {ans}")