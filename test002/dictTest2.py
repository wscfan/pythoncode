dict1 = {
    'name': '张三',
    'age': 19,
    'birth': '1993-06-15',
    'salary': 10000
}
print(dict1)
dict1['name'] = '李四'
print(dict1)
dict1.update(name="王五", age=28)
print(dict1)
dict1['sex'] = '男'
print(dict1)
dict1.update(age=30, interest="打篮球")
print(dict1)
print(dict1.pop('sex'))
print(dict1)
dict1.popitem()
print(dict1)
dict1.clear()
print(dict1)
