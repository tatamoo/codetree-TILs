n = int(input())

num = list(map(int,input().split()))
pos = []
for i in num:
    if i%2==0:
        pos.append(i)

for j in range(len(pos)):
    print(pos[j], end=" ")
