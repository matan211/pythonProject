def doItems(d: dict):
    list1 = []
    for i in d:
        t1 = (i, d[i])
        list1.append(t1)
    return list1


d1 = {1: 10, 2: 20, 3: 30, 4: 40}
d2 = {'aaaa':23, 'bbb':342, 'ccc':234, 'ddd':'matan'}
print(doItems(d1))
print(doItems(d2))
