count = 0
num = int(input("enter number: "))
while num != 0:
    if num % 3 == 0 or num % 7 == 0:
        count += 1
    num = int(input("enter number: "))
print(count)
