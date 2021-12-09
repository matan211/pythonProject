num1 = int(input("enter 3-digit number: "))
first_dig = num1%10
second_dig = (num1//10)%10
third_dig = num1//100
num2 = third_dig + second_dig*10 + first_dig*100
print(num2)
