def from_num_to_num(num, num1):
    for i in range(num, num1 + 1):
        print(i, end=" ")


num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))


# exercise 7
def return_min(num, num1):
    if num1 < num:
        return num1
    else:
        return num


def return_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


maximum = return_max(num1, num2)

minimum = return_min(num1, num2)
from_num_to_num(minimum, maximum)
