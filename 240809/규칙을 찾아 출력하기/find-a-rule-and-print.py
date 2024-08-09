n = int(input())

for _ in range(n):
    print("*",end=' ')
print()

for i in range(n-1):
    for j in range(n):
        if j==n-1 or j<=i:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print()