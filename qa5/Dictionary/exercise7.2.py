key = int(input("enter a key: "))
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
all_dic = {}
all_dic.update(dic1)
all_dic.update(dic2)
all_dic.update(dic3)
print(key in all_dic)
