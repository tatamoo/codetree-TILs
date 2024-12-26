n = list(map(int,input().split()))
arr = []
i=0
while 1:
    if n[i]==0:
        break
    arr.append(n[i])
    i+=1

for j in range(len(arr)):
    if(arr[j]%2==0):
        print(arr[j]//2,end=" ")
    else:
        print(arr[j]+3, end=" ")
    

    
