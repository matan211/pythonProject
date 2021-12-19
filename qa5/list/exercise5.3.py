# get a list of grade and print how many passed and how many failed
grade = int(input("enter grade: "))
list1 = []
# input of the list
while grade >= 0:
    list1.append(grade)
    grade = int(input("enter grade: "))

fail = 0
passed = 0
# the loop runs over the list
for i in range(len(list1)):
    if list1[i] < 60:
        fail += 1
    else:
        passed += 1

print(f"{passed} passed and {fail} failed")
