n = int(input())

for i in range(n):
    arr = list(map(str,input()))
    stack = []
    for j in arr:
        if len(stack) == 0:
            stack.append(j)
        else:
            last = stack.pop()
            if last == '(' and j==')':
                continue
            else:
                stack.append(last)
                stack.append(j)
    if len(stack)==0:
        print('YES')
    else:
        print('NO')