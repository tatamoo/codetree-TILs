a,b=input().split()
a,b=int(a),int(b)


print(f"{int(a//b)}.",end='')
a=float((a%b)*10)



i = 10
for _ in range(20):
    if a<b:
        print(0,end='')
        a *= 10
    else:
        print(int(a//b),end='')
        a = float((a%b)*10)