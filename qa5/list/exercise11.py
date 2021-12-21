list1 = [1, 1]
for i in range(2,10):
    list1.append(list1[i-2]+list1[i-1])
print(list1)
