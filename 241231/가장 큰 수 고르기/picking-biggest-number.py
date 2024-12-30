a = list(map(int, input().split()))
max = a[0]
for i in a[1:]:
    if max < i:
        max = i

print(max)
