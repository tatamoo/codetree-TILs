n = int(input())
cnt_f = 1
cnt_s = n
for _ in range(n):
    for i in range(n):
        if i%2==0:
            print(cnt_f,end='')
        else:
            print(cnt_s,end='')
           
    print()
    cnt_f += 1
    cnt_s -= 1