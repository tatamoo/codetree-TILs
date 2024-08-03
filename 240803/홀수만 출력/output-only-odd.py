a,b = input().split()
a,b=int(a),int(b)

for i in range(a,b+1):
    if(i%2!=0):
        print(i, end=' ')