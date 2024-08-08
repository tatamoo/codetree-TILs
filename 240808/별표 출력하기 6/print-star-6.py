n = int(input())

for i in range(n):
    for _ in range(i):
        print(" ",end=' ')
    for _ in range((n-i)*2-1):
        print("*",end=' ')
    print()

for j in range(1,n):
    for _ in range(n-j-1):
        print(" ",end=' ')
    for _ in range(j*2+1):
        print("*",end=' ')
    print()