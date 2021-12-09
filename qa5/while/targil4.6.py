str1 = input("enter string: ")
char1 = input("enter char: ")
i = 0
counter = 0
while i in range(str1.__len__()):
    if char1 == str1[i]:
       counter += 1
    i += 1

print(counter)
