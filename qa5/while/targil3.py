num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
while num1 % 2 == 0 and num2 % 2 == 0:
    print(num1 + num2)
    num1 = int(input("enter number: "))
    num2 = int(input("enter number: "))
print(num1 + num2)
