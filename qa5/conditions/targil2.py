num1 = input("enter number: ")
if num1 == '' or int(num1) >= 1000 or int(num1) < 100:
    print("invalid input")
else:
    num1 = int(num1)
    print((num1%10) + ((num1 // 10) % 10) + (num1//100))
