a,b = input().split()

a,b = int(a),int(b)

while a<=b:
    if a%2 == 0:
        print(a,end=' ') 
        a += 2
    else:
        a += 1