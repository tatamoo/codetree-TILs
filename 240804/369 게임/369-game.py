n = int(input())

for i in range(1,n+1):
    if i%3==0:
        print(0,end=' ')
    else:
        if i<10:
            print(i,end=' ')
        else:
            temp = string(i).split('')
            for i in range(0,2):
                if temp[i]=='3'or temp[i]=='6' or temp[i]=='9':
                    print(0,end=' ')
                    break
            print(i,end=' ')