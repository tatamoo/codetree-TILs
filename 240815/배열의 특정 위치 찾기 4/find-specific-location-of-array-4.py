arr = list(map(int,input().split()))
cnt = 0
sum = 0
even = 0

for elem in arr:
    if elem==0:
        for i in range(cnt):
            if arr[i]%2==0:
                sum += arr[i]
                even += 1
        break
    else:
        cnt += 1

print(even,sum)