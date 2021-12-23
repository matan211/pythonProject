from random import randint

words = ["hangman", "chairs", "backpack", "bodywash", "clothing", "computer", "python", "program", "glasses",
         "sweatshirt", "sweatpants", "mattress", "friends", "clocks", "biology", "algebra", "suitcase", "knives",
         "ninjas", "shampoo"]
word = words[randint(0, len(words) - 1)]
# print(word)
current = "_" * len(word)
print(current)
trials = 1


def putTheletter(current, word, letter):
    indexes = []
    for i in range(len(word)):
        if word[i] == letter:
            indexes.append(i)
    for i in indexes:
        current = current[:i] + letter + current[i + 1:]
    return current


while trials <= 10 and current != word:
    letter = input("enter a letter: ")
    if letter in current:
        print("letter already found! try another one")
    else:
        current = putTheletter(current, word, letter)
        trials += 1
    print(current)

if trials > 10:
    print("You failed! try again")
    print(f"the word is {word}")
else:
    print("You success!")
