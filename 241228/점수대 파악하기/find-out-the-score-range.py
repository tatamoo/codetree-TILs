cnt = [0] * 11
arr = list(map(int, input().split()))
i = 0

while arr[i]!=0:
    cnt[arr[i]//10] += 1
    i += 1
for j in range(10,0,-1):
    print(f"{j*10} - {cnt[j]}")