tc = int(input())

while tc:
    y = x = 0
    y, x = map(int, input().split())
    num = 0
    if y % 2 == 0: # max is x^2 ,  x - odd
        num = (y**2) - (x-1)
    elif x % 2 == 1 : # max is y^2,   y - even
        num = (y**2) + (x+1)
    print(num)

    tc -= 1