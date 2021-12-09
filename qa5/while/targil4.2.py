num = int(input("enter number: "))
isPrime = True
i = 2
while i in range(2, num):
    if num % i == 0:
        isPrime = False
    i += 1
if isPrime:
    print("prime")
else:
    print("not - prime")
