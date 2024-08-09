n = int(input())

for _ in range(n):
    print("*",end=' ')
print()

if n%2==0:
    for i in range(n-1):
        for j in range(n):
            if j<=i or j%2==0:
                print(" ",end=' ')
            else:
                print("*",end=' ')
        print()
else:
    for i in range(n-2):
        for j in range(n):
            if j<=i or j%2==0 or :
                print(" ",end=' ')
            else:
                print("*",end=' ')
        print()