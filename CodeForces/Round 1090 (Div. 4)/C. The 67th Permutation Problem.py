t = int(input())

while (t):
    x = int(input())
    a = []
    max  = 3*x
    b=1
    median = max - 1

    for i in range (x,0,-1):
        a.append(b)
        b += 1
        a.append(median)
        a.append(median+1)
        median -= 2

    print(*a)

    t -= 1