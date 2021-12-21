from random import randint
list1 = [randint(1, 100) for i in range(10)]
print(list1)
t1 = tuple(list1)
print(t1)
# num = int(input("enter a number: "))
# t1 += (num,)
# print(t1)
list2 = list(t1)
t2 = tuple(list2[0:4])
for i in range(len(list2)-4, len(list2)):
    t2 += (list2[i],)
print(t2)

list2 = list(t2)
list2 = list2[1:len(list2)]
print(list2)
t2 = tuple(list2)
print(t2)
