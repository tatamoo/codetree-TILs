n = int(input())
cnt = [0] * 10
arr = list(map(int,input().split()))

for j in range(n):
    cnt[arr[j]] += 1

for i in range(1,10):
    print(cnt[i])

