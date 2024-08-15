n = int(input())
arr = list(map(int,input().split()))
even = list()

for elem in arr[n-1::-1]:
    if elem%2==0:
        even.append(elem)

for i in range(len(even)):
    print(even[i],end=' ')