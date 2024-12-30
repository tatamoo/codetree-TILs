n, q = input().split()
n, q = int(n), int(q)

arr = list(map(int,input().split()))

for _ in range(q):
    qq = list(map(int, input().split()))
    if qq[0]==1:
        print(arr[qq[1]-1])
    elif qq[0]==2:
        if qq[1] in arr:
            print(arr.index(qq[1])+1)
        else:
            print(0)
    elif qq[0]==3:
        for i in range(qq[1]-1,qq[2]):
            print(arr[i],end=" ")
        print()