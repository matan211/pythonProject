num = input("enter number: ")
if num == '':
    print("invalid input")
else:
    num = int(num)
    if num % 2 == 0:
        print("zugi")
    else:
        print("e-zugi")
