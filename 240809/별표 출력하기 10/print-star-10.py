n = int(input())

for i in range(n*2):
    if i%2!=0:
        for _ in range(n-int((i-1)/2)):
            print("*",end=' ')
        print()
    else:
        for _ in range(1+int((i/2))):
            print("*",end=' ')
        print()