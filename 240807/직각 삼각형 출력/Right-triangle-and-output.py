n = int(input())
r = 0

for i in range(n):
    j = i + (i+1)
    for _ in range(j):
        print("*",end='')
    print()