a,b = input().split()
a,b = int(a),int(b)

arr = [0,0]
arr[0] = a
arr[1] = b

for i in range(2, 10):
    result = arr[-1] + arr[-2]
    if result>=10:
        result = result%10
    arr.append(result)

for j in range(10):
    print(arr[j],end=" ")