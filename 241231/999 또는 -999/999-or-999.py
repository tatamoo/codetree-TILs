a = list(map(int, input().split()))
min = a[0]
max = a[0]

for i in a[1:]:
    if i == 999 or i == -999:
        break

    if min > i:
        min = i
    
    if max < i:
        max = i

print(max, min)