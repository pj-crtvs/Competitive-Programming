n = int(input())
a = list(map(int, input().split()))

move = 0
cntrmove = 0
for i in range(1, n):
    if a[i] < a[i-1]:
        move += a[i-1] - a[i]
        a[i] += a[i-1] - a[i]
print(move)
