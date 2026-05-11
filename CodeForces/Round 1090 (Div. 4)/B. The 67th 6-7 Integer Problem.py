t = int(input())

while t:
    x = sorted(list(map(int, input().split())))
    print((x[-1]) - sum(x[:-1]))
    t -= 1