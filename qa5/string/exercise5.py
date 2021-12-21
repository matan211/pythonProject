text = input("enter text: ")
c1 = input("enter text: ")
count = 0
for i in range(len(text)):
    if text[i] == c1:
        count += 1

print(count)
