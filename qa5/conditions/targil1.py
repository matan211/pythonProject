num1 = input("enter number: ")
num2 = input("enter number: ")
if num1 == '' or num2 == '':
    print("invalid input")
elif ((int(num1) + int(num2)) % 2 == 0):
    print("zugi")
else:
    print("e-zugi")
