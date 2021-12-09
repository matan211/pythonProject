age = input("enter age: ")
if age == '' or int(age) < 0 or int(age) > 120:
    print("invalid input")
if age == '':
    age = -1
age = int(age)
if( 0 <= age <= 18):
    print("child")
elif( 19 <= age <= 60):
    print("adult")
elif( 61 <= age <= 120):
    print("senior")
