lst = [10 * i for i in range(0, 10)]
print(lst)
lst2 = [10 * i for i in range(0, 10) if i % 2 == 0]
print(lst2)
lst3 = [i * j for i in range(0, 3) for j in range(0, 3)]
print(lst3)
lst4 = ["张三", "李四", "王五"]
dict1 = {i+1: lst4[i] for i in range(0, len(lst4))}
print(dict1)
set1 = {i * j for i in range(1, 5) for j in range(1, 5) if i == j}
print(set1)