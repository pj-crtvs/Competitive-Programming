DNA = input()
count = 1
max = 1

for i in range(1, len(DNA)):
    if DNA[i] == DNA[i-1]:
        count += 1
    if count > max:
        max = count
    if DNA[i] != DNA[i-1]:
        count = 1

print(max)