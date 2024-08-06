while True:
    answer = int(input())
    if answer < 25:
        print("Higher")
    elif answer >25:
        print("Lower")
    else:
        print("Good")
        break