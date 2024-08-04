n = int(input())

cntc = 0
cnth = 0
cntb = 0


for i in range(1,n+1):
    if i%12==0:
        cntb += 1
    elif i%3==0:
        cnth += 1
    elif i%2==0:
        cntc += 1
    
print(cntc,cnth,cntb)