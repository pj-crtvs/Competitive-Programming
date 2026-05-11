n = int(input())
a = list(map(int, input().split()))

s = int(n*(n+1) /2)
sa = sum(a)
m = s - sa

print(m)