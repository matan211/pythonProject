def isValid(num):
    if num >= 100 and num <= 999:
        return True
    else:
        return False

num = int(input("enter a number: "))
if isValid(num):
    print("valid")
else:
    print("invalid")
