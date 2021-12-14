import math
num = int(input("enter number: "))


def isPrime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for i in range(4):
    num1 = int(input("enter number: "))
    if isPrime(num):
        num = min(num, num1)
print(num)

