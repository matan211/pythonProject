set1 = {1, 2, 3, 4, 5, 6}
set2 = {5, 6, 7, 8, 9}
combine_set = set()
for i in set1:
    combine_set.add(i)
for i in set2:
    combine_set.add(i)

print(combine_set)
combine_set.pop()
print(combine_set)
new_set = set(combine_set)
print(new_set)
maximum = set1.pop()
minimum = maximum
for i in combine_set:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
print(f"max is: {maximum}")
print(f"min is: {minimum}")
print(f"length is: {len(combine_set)}")
new_set.add(10)
new_set.add(11)
set1.clear()
set2.clear()
print(new_set)
print(set1)
print(set2)
