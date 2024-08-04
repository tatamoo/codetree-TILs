n = int(input())

arr = []
num = 0

for _ in range(n):
    temp = int(input())
    if temp%2!=0 and temp%3==0:
        arr.append(temp)
        num += 1

for i in range(num):
    print(arr[i])