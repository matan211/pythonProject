text1 = input("enter text: ")
text2 = input("enter text: ")
common = ""
for i in text1:
    if text2.count(i) > 0 and common.count(i) == 0:
        common += i

print(len(common))
