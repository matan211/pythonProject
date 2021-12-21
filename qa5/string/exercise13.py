sentence = input("enter text: ")
character = input("enter text: ")
sentence_list = []
new_sentence = ""

for i in sentence:
    sentence_list.append(i)
print(sentence_list)
for i in range(len(sentence_list)):
    if sentence_list[i] == character:
        sentence_list[i] = character.upper()

print(sentence_list)
for i in sentence_list:
    new_sentence += i
print(new_sentence)
