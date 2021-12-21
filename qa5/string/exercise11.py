text = input("enter text: ")
word = input("enter text: ")
list_text = text.split(' ')
list_index = []
# print(list_text)
index = 0
for i in range(len(list_text)):
    if list_text[i] == word:
        list_index.append(0)
        for l in range(0, i):
         list_index[index] += len(list_text[l])+1
        index += 1

print(list_index)
