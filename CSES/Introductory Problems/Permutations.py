n = int(input())
arr = []
flag = False

if n == 1:
    print(1)
elif n < 4:
    print("NO SOLUTION")
else:
    k = n-1
    while k > 0:
        arr.append(k)
        k -= 2

    k = n
    while k > 0:
        arr.append(k)
        k -= 2

    for i in range(1, n):
        if arr[i] - arr[i-1] == 1:
            print("NO SOLUTION")
            break
        flag = True
    if flag:
        print(*arr)