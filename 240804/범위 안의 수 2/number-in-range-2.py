sum_val = 0
cnt = 0

for _ in range(10):
    temp = int(input())
    if temp>=0 and temp<=200:
        sum_val += temp
        cnt += 1

print(f"{sum_val} {sum_val/cnt:.1f}")