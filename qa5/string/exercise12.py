sentence = input("enter text: ")
list_text = sentence.split(' ')
new_sentence = ""
print(list_text)
for word in list_text:
    new_sentence += word.capitalize() + " "

print(new_sentence)

