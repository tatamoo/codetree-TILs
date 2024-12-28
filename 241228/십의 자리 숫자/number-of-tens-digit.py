cnt = [0] * 10
arr = list(map(int, input().split()))
i = 0

while arr[i] != 0:
    if arr[i]>=10:
        cnt[arr[i]//10] += 1
    i += 1
    
for j in range(1,10):
    print(f"{j} - {cnt[j]}")