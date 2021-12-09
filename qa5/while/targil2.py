age = int(input("enter age: "))
while (age <= 120) and age >= 0:
    if (age >= 0) and age <= 18:
        print("child")
    elif (age >= 19) and age <= 60:
        print("adult")
    elif (age >= 61) and age <= 120:
        print("senior")
    age = int(input("enter age: "))
