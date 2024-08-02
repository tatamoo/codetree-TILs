am,ae = input().split()
am,ae = int(am),int(ae)
bm,be = input().split()
bm,be = int(bm),int(be)

if am>bm:
    print("A")
elif am<bm:
    print("B")
elif ae>be:
    print("A")
elif ae<be:
    print("B")