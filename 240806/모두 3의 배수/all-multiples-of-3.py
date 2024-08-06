result = True
for _ in range(5):
    num = int(input())
    if num%3!=0:
        result=False

if result == False:
    print(0)
else:
    print(1)