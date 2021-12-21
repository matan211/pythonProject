text = input("enter text: ")
new_text = ""
for i in text:
    if text.count(i) > 1 and new_text.count(i) == 0:
        new_text += i

print(new_text)
