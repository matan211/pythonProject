import random

guess = random.randint(0, 100)
isEquivilant = False
answer = ""
numberOfSuggestions = 1
while isEquivilant == False:
    print(f"Is the number {guess}?")
    answer = input()
    if answer == "yes":
        isEquivilant = True
    elif answer == "bigger" or answer == "smaller":
        numberOfSuggestions += 1
        guess = random.randint(0, 100)
if isEquivilant:
    print(numberOfSuggestions)
