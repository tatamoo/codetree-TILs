n = int(input())

for i in range(n):
    for _ in range(n-i-1):
        print(" ",end='')
    for _ in range(i+1):
        print("*",end=' ')
    print()
for j in range(1,n):
    for _ in range(j):
        print(" ",end='')
    for _ in range(n-j):
        print("*",end=' ')
    print()