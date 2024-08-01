height,weight = input().split()
height,weight = int(height),int(weight)
bmi = int(10000*weight/height**2)
print(bmi)
if bmi>=25:
    print("Obesity")