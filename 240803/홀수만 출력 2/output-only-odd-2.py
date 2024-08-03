b,a = input().split()
b,a = int(b),int(a)

for i in range(b,a-1,-1):
    if(i%2!=0):
        print(i,end=' ')