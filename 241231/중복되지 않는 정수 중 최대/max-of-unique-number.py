n = int(input())
a = list(map(int, input().split()))
c = [0]*(n+1)
max = 0

for i in range(len(a)):
    c[a[i]] += 1

for j in range(len(c)):
    if c[j]==1:
        max = j

if max == 0:
    print(-1)
else:
    print(max)