year = int(input("enter year: "))
leapY = False
if year % 100 == 0:
    if year % 400 == 0:
        leapY = True
elif year % 4 == 0:
    leapY = True
if leapY:
    print("leap year")
else:
    print("not leap year")