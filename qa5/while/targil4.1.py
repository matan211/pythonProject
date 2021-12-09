num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
num1 += 1
while num1 < num2:
    if num1 % 2 == 0:
        print(num1)
    num1 += 1
