num1 = int(input("enter number: "))
while (num1 < 1000) and num1 >= 100:
    dig3 = num1 % 10
    dig2 = num1//10 % 10
    dig1 = num1//100
    new_num = dig3 + dig2 + dig1
    print(dig3+dig2+dig1)
    num1 = int(input("enter number: "))
print("invalid input")
