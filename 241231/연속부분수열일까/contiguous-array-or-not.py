n1, n2 = input().split()
n1, n2 = int(n1), int(n2)

a = list(map(int,input().split()))
b = list(map(int,input().split()))

y = 0
for i in range(len(a)):
    if a[i] == b[0]:
        for j in range(1,len(b)):
            if a[i+j] != b[j]:
                break
            
            if j==len(b):
                y = 1
                print("Yes")

if y!=1:
    print("No")
        
        
