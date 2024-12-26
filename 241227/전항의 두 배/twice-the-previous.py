a, b = input().split()
a,b = int(a),int(b)
arr = []
arr.append(a)
arr.append(b)

for i in range(2,10):
    arr.append(arr[-1] + arr[-2]*2 )

for j in range(10):
    print(arr[j], end=" ")