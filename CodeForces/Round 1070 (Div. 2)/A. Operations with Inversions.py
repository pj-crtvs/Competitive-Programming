tc = int(input())

while tc:
    tc -= 1
    n = int(input())
    a = list(map(int, input().split()))
    maxx = a[0]
    count = 0

    for i in range (n):
        if maxx > a[i]:
            count += 1
        else:
            maxx = a[i]


    print(count)