from random import randint

words = ["book", "paper", "notebook", "window", "bottle", "water", "wallet", "key", "remote"]
print("there are", len(words), "words")

word = words[randint(0, len(words)-1)]
print(word)

fails = 0
currentOutput = "_"*len(word)
print(currentOutput)


def putTheLetter(newWord, word, letter):
    


while fails < 8:
    letter = input("enter letter: ")
    if word.find(letter) == -1:
        fails += 1
    else:
        currentOutput = putTheLetter(currentOutput, word, letter)
    print(currentOutput)
