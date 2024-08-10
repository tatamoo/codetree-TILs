n = int(input())
p = int(11)
for i in range(1,n+1):
    for _ in range(n):
        print(f"{p}",end=' ')
        p += 2
    print()
    p = 11 + 2*i