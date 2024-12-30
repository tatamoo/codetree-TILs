import sys

n = int(input())
a = list(map(int, input().split()))
c = [0]*(n+1)
max = -sys.maxsize

for i in range(len(a)):
    c[a[i]] += 1

for i in range(len(c)):
    if c[i]==1:
        if max<c[i]:
            max = i

if max == -sys.maxsize:
    print(-1)
else:
    print(max)