num = int(input("enter number: "))
i = 0
if i == 1:
    print(0)
lastN = 1
secondLastN = 0
while i in range(num):
    print(secondLastN)
    lastN += secondLastN
    secondLastN = lastN - secondLastN
    i += 1