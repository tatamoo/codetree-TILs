mid, fin = input().split()
mid, fin = int(mid),int(fin)

if mid<90:
    print(0)
elif fin>=95:
    print(100000)
elif fin>=90:
    print(50000)
else:
    print(0)