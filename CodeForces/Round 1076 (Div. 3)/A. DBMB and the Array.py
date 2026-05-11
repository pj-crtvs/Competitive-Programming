tc = int(input())

while tc:
    tc -= 1
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range (n):
        if a[i] < b[i]:
            a[i] = b[i]
    for i in range (n-1, 1, -1):
        if a[i-1] < a[i]:
            a[i-1] = a[i]

    rsum = [0] * (n)
    rsum[0] = a[0]

    for i in range(1, n):
        rsum[i] = rsum[i-1] + a[i]

    while (q):
        q -= 1
        l,r = map(int, input().split())

        if (l != 1):
            ans = rsum[r-1] - rsum[l-2]
        else:
            ans = rsum[r-1]

        print(ans, end=" ")

    print()




