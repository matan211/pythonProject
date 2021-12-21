list1 = []
for i in range(1,11):
    list1.append(i)
list2 = list1[7:]
print(list2)
print(list1[::-1])
print(list1[::2])
listEZugi = list1[::2]
print(listEZugi)
#
#list1[4] = int(input("enter number: "))
#list1[5] = int(input("enter number: "))
#list1.append(int(input("enter number: ")))
#print(list1)

listP2 = []
for i in range(len(list1)):
    listP2.append(list1[i]*2)
print(listP2)
firstAndLast = [list1[0], list1[len(list1)-1]]
print(firstAndLast)
