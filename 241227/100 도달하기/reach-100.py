n = int(input())

arr = []
arr.append(1)
arr.append(n)

while arr[-1]<=100:
    arr.append(arr[-1]+arr[-2])

for i in range(len(arr)):
    print(arr[i], end=" ")