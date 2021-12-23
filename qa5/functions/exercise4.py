# num = int(input("enter a number: "))


def sum_unti_the_num(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print(sum)

# exercise 5
for i in range(5):
    sum_unti_the_num(int(input("enter a number: ")))
