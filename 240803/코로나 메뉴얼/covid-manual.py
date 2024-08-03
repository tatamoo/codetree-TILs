a, a_tem = input().split()
a_tem = int(a_tem)
b, b_tem = input().split()
b_tem = int(b_tem)
c, c_tem = input().split()
c_tem = int(c_tem)

num = 0;

if a=='Y' and a_tem>=37:
    num += 1

if b=='Y' and b_tem>=37:
    num += 1

if c=='Y' and c_tem>=37:
    num += 1

if num>=2:
    print("E")
else:
    print("N")