a,b = input().split()
a,b = int(a),int(b)
result = False
for i in range(a,b+1):
    if 1920%1==0 and 2880%i==0:
        result = True

if result == True:
    print(1)
else:
    print(0)