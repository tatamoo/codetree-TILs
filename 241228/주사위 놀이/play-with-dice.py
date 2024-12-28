cnt = [0]*7
arr = list(map(int, input().split()))

for i in range(10):
    cnt[arr[i]] += 1

for j in range(1,7):
    print(f"{j} - {cnt[j]}")

