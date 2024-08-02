a,b,c = input().split()
a,b,c=int(a),int(b),int(c)

if a<=b and a<=c:
    print(1, end = " ")
else:
    print(0, end = " ")

if a==b and b==c:
    print(1, end = " ")
else:
    print(0, end = " ")