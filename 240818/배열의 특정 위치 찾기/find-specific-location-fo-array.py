arr = list(map(int,input().split()))
even = arr
sum_val=sum(arr[1::2])
three_sum = sum(arr[2::3])
print(f"{sum_val} {three_sum/len(arr[2::3]):.1f}")