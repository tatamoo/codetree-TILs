n = int(input())

for _ in range(n):
    print("*",end=' ')
print()

for i in range(n-1):
    for j in range(n):
        if j==n-1:
            print("*",end=' ')
        else:
            for _ in range(i):
                print("*",end=' ')
            for _ in range(n-i-1):
                print(" ",end=' ')