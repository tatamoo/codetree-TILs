n = int(input())
cnt = 0
for i in range(1,n+1):
    n = int(n/i)
    if n<=1:
        cnt += 1
        break
    else:
        cnt += 1

print(cnt)