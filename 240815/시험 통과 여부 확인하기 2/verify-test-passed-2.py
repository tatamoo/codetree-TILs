n = int(input())
cnt = 0
for _ in range(n):
    arr = list(map(int,input().split()))
    if sum(arr)/len(arr)>=60:
        print("pass")
        cnt += 1
    else:
        print("fail")
print(cnt)