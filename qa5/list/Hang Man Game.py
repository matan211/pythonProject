from random import randint

words = ["book", "paper", "notebook", "window", "bottle", "water", "wallet", "key", "remote"]
print("there are", len(words), "words")

word = words[randint(0, len(words) - 1)]
print(word)

fails = 0
currentOutput = "_" * len(word)
print(currentOutput)


def putTheLetter(newWord, word, letter):
    list_newWord = []
    list_word = []
    word1 = ""
    for i in word:
        list_word.append(i)
    for i in newWord:
        list_newWord.append(i)
    for i in range(len(list_word)):
        if list_word[i] == letter:
            if list_newWord[i] == "_":
                list_newWord[i] = letter
                break

    for i in list_newWord:
        word1 += i
    return word1


while fails < 8 and word != currentOutput:
    letter = input("enter letter: ")
    if word.find(letter) == -1:
        fails += 1
    else:
        currentOutput = putTheLetter(currentOutput, word, letter)
    print(currentOutput)
if fails < 8:
    print(f"you succeded in {fails+len(word)} tries")
else:
    print("you failed")
