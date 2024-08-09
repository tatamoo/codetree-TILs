n = int(input())

for i in range(1,n*2+1):
    if i%2==0:
        for _ in range(int(i/2)):
            print("*",end=' ')
        print()
    else:
        for _ in range(n-int(i/2)):
            print("*",end=' ')
        print()