def only_once(list1: list):
    s1 = set()
    for i in list1:
        s1.add(i)
    return list(s1)

list1 = [1, 2, 3, 3, 3, 3, 4, 5]
print(only_once(list1))
