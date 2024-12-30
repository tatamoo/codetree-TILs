n = int(input())
a = list(map(int, input().split()))
c = [0] * n
max = 0

for i in range(n):
    c[a[i]-1] += 1

for j in range(n):
    if c[j] == 1:
        max = j+1

if max == 0:
    print(-1)
else:
    print(max)