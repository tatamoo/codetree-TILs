b,a = input().split()
b,a = int(b),int(a)

while b>=a:
    if b%2==0:
        print(b,end=' ')
        b -= 2
    else:
        b -= 1