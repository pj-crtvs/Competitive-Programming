tc = int(input())

while tc:
    tc -= 1
    n = int(input())
    str = input()
    str2 = str + str
    count = 0
    maxx = 0

    #
    for i in range (len(str2)):
        if str2[i] == '0':
            maxx += 1
        elif str2[i] == '1':
            if count < maxx:
                count = maxx
            maxx = 0
    print(count)

