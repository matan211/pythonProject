import random
num = random.randint(1, 9)
guess = int(input("enter number: "))
while guess != num:
    if guess > num:
        print("too big")
    elif guess < num:
        print("too small")
    guess = int(input("enter number: "))
if num == guess:
    print("you right")