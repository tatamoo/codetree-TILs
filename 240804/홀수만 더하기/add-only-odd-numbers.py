n = int(input())
sum_val = 0
for _ in range(n):
    temp = int(input())
    if temp%2!=0 and temp%3==0:
        sum_val += temp

print(sum_val)