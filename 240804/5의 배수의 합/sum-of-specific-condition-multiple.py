a,b = input().split()
a,b = int(a),int(b)
sum_val = 0
if a>b:
    for i in range(a,b+1):
        if i%5==0:
            sum_val += i
else:
    for i in range(b,a+1):
        if i%5==0:
            sum_val += i

print(sum_val)