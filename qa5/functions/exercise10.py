def isPassed(grade):
    if 70 <= grade <= 100:
        return True
    else:
        return False


for i in range(5):
    grade = int(input("enter a grade: "))
    print(isPassed(grade))
