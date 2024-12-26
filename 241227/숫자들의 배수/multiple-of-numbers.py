n = int(input())

cnt = 0
i = 1
arr = []

while 1:
    if(cnt==2):
        break
    
    arr.append(n*i)
    print(arr[i-1],end=" ")

    if(arr[i-1]%5==0):
        cnt+=1

    i+=1
