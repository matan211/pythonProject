num1 = int(input("enter number: "))
num2 = int(input("enter number: "))
if num2 >= num1:
    print("invalid input")
result = 0
for i in range(num2, num1+1, num2):
    result+=1
print("result is: ", result)
print("modulo is: ", num1-(result*num2))
