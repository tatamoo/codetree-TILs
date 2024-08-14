n = int(input())
cnt = 0
start = 0
for i in range(n):
    if i%2!=0:
        start = cnt + n + 1
        cnt += n

    for _ in range(n):
        if i%2==0:
            cnt+=1
            print(cnt,end=' ')
        else:
            start-=1
            print(start,end=' ')
    print()