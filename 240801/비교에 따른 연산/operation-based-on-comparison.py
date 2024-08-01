a,b = input().split()
a,b = int(a),int(b)

if a>b:
    print(int(a*b))
else:
    print(int(b//a))