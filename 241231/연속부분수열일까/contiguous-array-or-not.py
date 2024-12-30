n1, n2 = input().split()
n1, n2 = int(n1), int(n2)

a = list(map(int,input().split()))
b = list(map(int,input().split()))

y = 0
for i in range(n1):
    if a[i] == b[0]:
        for j in range(1,n2):
            if (i+j) == n1 or a[i+j] != b[j]:
                break
            
            if j == n2-1:
                y = 1
                print("Yes")

if y != 1:
    print("No")
        
        
