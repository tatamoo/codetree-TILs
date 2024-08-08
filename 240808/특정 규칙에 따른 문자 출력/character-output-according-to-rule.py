n = int(input())

for i in range(n):
    for _ in range(n-1-i):
        print(" ",end=' ')
    for _ in range(i+1):
        print("@",end=' ')
    print()
for j in range(n-1):
    for _ in range(n-1-j):
        print("@",end=' ')
    print()