n = int(input())
sum_val=0

for _ in range(n):
    temp = int(input())
    sum_val += temp

print(sum_val,f"{sum_val/n:.1f}")