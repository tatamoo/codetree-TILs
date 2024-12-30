n = int(input())
a = list(map(int, input().split()))

min = a[0]
for i in a[1:]:
    if i < min:
        min = i

cnt = 0
for i in a:
    if i == min:
        cnt += 1

print(min, cnt)