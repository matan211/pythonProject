text = input("enter text: ")
new_text = ""

for i in range(len(text)):
    if text[i] != 'a' and text[i] != 'A':
        new_text += text[i]

print(new_text)
