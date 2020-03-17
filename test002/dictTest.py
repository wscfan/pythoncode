dict1 = {}
print(type(dict1))
dict2 = {
    "name": "张三",
    "age": 19,
    "job": "程序猿"
}
print(dict2)
dict3 = dict(name='李四', sex=19)
print(dict3)
dict4 = dict.fromkeys(['老一', '老二', '老三', '老四'], 0)
print(dict4)
print(dict3['name'])
print(dict3.get('sex'))
print(dict3.get('aaa', '其他'))
print('老一' in dict4)
print('老一' not in dict4)
for key in dict3:
    print(dict3[key])

print('-----------------')

for key, value in dict3.items():
    print(key, value, end="\t")
