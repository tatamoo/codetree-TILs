n = int(input())
a = list(map(int, input().split()))
b = [0] * len(a)
mx = 0
for i in range(len(a)):
    mx = max(a)
    b[i] = mx
    a[a.index(mx)] = min(a)

print(b[0],b[1])