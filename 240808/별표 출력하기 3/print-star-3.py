n = int(input())

for i in range(n):
    for _ in range(i):
        print(" ",end=" ")

    for _ in range((n-i)*2-1,0,-1):
        print("*",end=' ')
    print()