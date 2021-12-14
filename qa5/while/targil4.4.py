# this function suggest the number
import random
# range of random
minimum = 0
maximum = 100
guess = random.randint(minimum, maximum)
isEquivalent = False
answer = ""
numberOfSuggestions = 1
# isEquivalent == False
while not isEquivalent:
    print(f"Is the number {guess}?")
    answer = input()
    if answer == "yes":
        isEquivalent = True
    elif answer == "bigger":
        numberOfSuggestions += 1
        minimum = max(minimum, guess)
        guess = random.randint(minimum, maximum)
    elif answer == "smaller":
        numberOfSuggestions += 1
        maximum = min(maximum, guess)
        guess = random.randint(minimum, maximum)
if isEquivalent:
    print("number of suggestions is: ", numberOfSuggestions)
