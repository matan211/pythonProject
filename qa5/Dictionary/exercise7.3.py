dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
all_dic = {}
all_dic.update(dic1)
all_dic.update(dic2)
all_dic.update(dic3)
print(all_dic)
med = 0
new_dic = {}
for i in all_dic:
    new_dic[all_dic[i]] = i
print(new_dic)
