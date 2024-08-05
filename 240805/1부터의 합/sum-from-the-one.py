n = int(input())
val = 0
for i in range(1,100):
    val += i
    if val>=n:
        print(i)
        break