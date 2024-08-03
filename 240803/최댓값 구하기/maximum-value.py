a,b,c = input().split()
a,b,c = int(a),int(b),int(c)

if a>=b:
    if a>=c:
        print(a)
    else:
        print(c)
else:
    if b>=c:
        print(b)
    else:
        print(c)