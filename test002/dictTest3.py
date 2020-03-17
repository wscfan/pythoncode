dict1 = {'name': '张三', 'age': 19}
dict1.setdefault('salary', 2880)
print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
str = "姓名{name} 年龄{age}".format_map(dict1)
print(str)