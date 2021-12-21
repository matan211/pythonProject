list1 = []
text = input("enter text: ")

for i in text:
    list1.append(i)
    list1.append(i)

# print(list1)
new_text = ""
for i in list1:
    new_text += i

print(new_text)
