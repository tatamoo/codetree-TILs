arr = input().split()

arr[0],arr[1],arr[2] = int(arr[0]),int(arr[1]),int(arr[2])

if arr[0]>arr[1]:
    arr[0],arr[1] = arr[1],arr[0]
    if arr[1]>arr[2]:
        arr[1],arr[2] = arr[2],arr[1]
elif arr[1]>arr[2]:
    arr[1],arr[2] = arr[2],arr[1]

print(arr[1])