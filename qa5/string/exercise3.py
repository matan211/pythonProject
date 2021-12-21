text = input("enter text: ")
c1 = input("enter text: ")
found = False
index1 = -1
for i in range(len(text)):
    if text[i] == c1 and not found:
        index1 = i
        found = True

print(index1)
