num = 0
list1 = []
list2 = []
while num >= 0:
    list1.append(num)
    num = int(input("enter number for list 1: "))
num = 0
while num >= 0:
    list2.append(num)
    num = int(input("enter number for list 2: "))
print(len(list1) + len(list2))

