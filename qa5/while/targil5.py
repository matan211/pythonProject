num = int(input("enter number: "))
while (num >= 10) and num < 100:
    if num % 7 == 0:
        print("lucky number")
    elif num // 10 == 7 or num % 10 == 7:
        print("lucky number")
    else:
        print("not lucky number")
    num = int(input("enter number: "))
