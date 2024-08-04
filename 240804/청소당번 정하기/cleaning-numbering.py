n = int(input())

cntc = 0
cnth = 0
cntb = 0

datec = 2
dateh = 3
dateb = 12

for i in range(0,n+1):
    if i==dateb:
        cntb += 1
        dateb += 12
        if i==datec:
            datec += 2
        elif i==dateh:
            dateh += 3
    elif i==dateh:
        cnth += 1
        dateh += 3
        if i==datec:
            datec += 2
    elif i==datec:
        cntc += 1
        datec += 2
    
print(cntc,cnth,cntb)