from random import randint

text = input("enter text: ")
password = ""
for i in range(6):
    password += text[randint(0,len(text)-1)]

print(password)
