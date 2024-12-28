cnt = [0] * 10
arr = list(map(int, input().split()))

for i in range(len(arr)-1):
    if arr[i]>=10:
        cnt[arr[i]//10] += 1
    
for j in range(1,10):
    print(f"{j} - {cnt[j]}")