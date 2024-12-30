n1, n2 = input().split()
n1, n2 = int(n1), int(n2)

a = list(map(int,input().split()))
b = list(map(int,input().split()))

if b[0] in a:
    y = 0
    for i in range(1,len(b)):
        if b[i] != a[a.index(b[0])+i]:
            print("No")
            y = 1
            break
    if y==0:
        print("Yes")
else:
    print("No")
    