a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
result = True
for i in range(a,b+1):
    if i%c==0:
      result = False


if result == False:
    print("NO")
else:
    print("YES")