n = int(input())
a = list(map(int, input().split()))

unique_nums = [num for num in a if a.count(num) == 1]

if unique_nums:
    print(max(unique_nums))
else:
    print(-1)