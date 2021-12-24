from random import randint


def getSet(l: list):
    s1 = set()
    new_l = []
    for i in l:
        if new_l.count(i) == 0:
            new_l.append(i)
    for i in new_l:
        s1.add(i)
    return s1


list1 = [randint(1, 100) for i in range(20)]
print(list1)
print(getSet(list1))
