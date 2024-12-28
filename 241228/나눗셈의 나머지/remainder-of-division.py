a,b = input().split()
a,b = int(a),int(b)
cnt = [0] * b

while a>1:
    cnt[a%b] += 1
    a = a//b

result = 0
for i in range(b):
    result += cnt[i]**2

print(result)
    