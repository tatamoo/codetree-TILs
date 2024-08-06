val = 0
cnt = 0
while True:
    age = int(input())
    if age<30:
        val += age
        cnt += 1
    else:
        break

print(f"{(val/cnt):.2f}")