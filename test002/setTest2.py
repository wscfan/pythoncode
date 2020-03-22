set1 = {"aaa", "bbb", "ccc", "ddd"}
set2 = {"ccc", "ddd", "eee", "fff"}
intersection1 = set1.intersection(set2)
print(intersection1)
# set1.intersection_update(set2)
# print(set1)
union1 = set1.union(set2)
print(union1)
difference1 = set1.difference(set2)
print(difference1)
difference2 = set1.symmetric_difference(set2)
print(difference2)