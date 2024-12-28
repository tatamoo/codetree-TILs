cnt = [0]*5

for _ in range(3):
    c, t = input().split()
    t = int(t)

    if c == 'Y':
        if t>=37:
            cnt[1] += 1
        else:
            cnt[3] += 1
    else:
        if t>37:
            cnt[2] += 1
        else:
            cnt[4] += 1

for i in range(1,5):
    print(cnt[i], end=" ")

if cnt[1] >=2 :
    print("E")    