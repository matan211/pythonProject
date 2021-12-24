from random import randint
def average(list:list):
    sum = 0
    for i in list:
        sum += i
    return sum/len(list)

names = ['Yossi', 'Avraham', 'Hanan', 'Neta', 'Cohen']
grades = [randint(1, 100) for i in range(5)]
print(grades)
d1 = {}
for i in range(len(grades)):
    d1[names[i]] = grades[i]
print(d1)
print('average is ', average(grades))
for i in d1:
    if d1[i] < 70:
        print(i, ' failed')
    else:
        print(i, 'passed')





