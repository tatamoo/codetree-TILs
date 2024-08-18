arr = list(map(int,input().split()))
sum_val = 0
for i in range(len(arr)):
    if arr[i]==0:
        for j in range(1,4):
            sum_val += arr[i-j]
        break

print(sum_val)