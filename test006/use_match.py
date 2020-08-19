import re

# 将正则表达式编译
pattern = re.compile(r'(hello)', re.I)

rest = pattern.match('Hello, world')
print(rest.string)
print(rest.re)
print(rest.group())
