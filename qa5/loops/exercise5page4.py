index = 1
num1 = int(input("enter number: "))
maximum = num1
for i in range(2,8):
    num2 = int(input("enter number: "))
    if num2>num1:
        num1 = num2
        index = i
print(index)
