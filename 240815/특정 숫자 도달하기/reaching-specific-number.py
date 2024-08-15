arr = list(map(int,input().split()))
sum = 0
average = 0
for i in range(10):
    if arr[i]>=250:
        for j in range(i):
            sum += arr[j]
        average = float(sum/i)
        break
    else:
        continue

if sum==0:   
    for elem in arr:
        sum += elem
    average = float(sum/10)

print(f"{sum} {average:.1f}")