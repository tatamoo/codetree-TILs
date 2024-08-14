a,b = input().split()
a,b=int(a),int(b)

for i in range(1,10):
    for j in range(b,a-1,-1):
        if j%2==0:
            print(f"{j} * {i} = {j*i}",end=' ')
            if j-1>a:
                print("/ ",end='')
        else:
            continue
    print()