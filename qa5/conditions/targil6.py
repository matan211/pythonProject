num1 = input("enter number: ")
num2 = input("enter number: ")
if num1 != '' and num2 != '':
    num1 = int(num1)
    num2 = int(num2)
    if (num1 + num2) == 10:
        print("sum is 10")
    else:
        print("sum is not 10")
else:
    print("invalid input")
