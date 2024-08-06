n = int(input())
result = True
for i in range(2,n):
    if n%i==0:
        result = False

if result==False:
    print("C")
else:
    print("P")