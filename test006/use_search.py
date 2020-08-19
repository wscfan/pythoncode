import re

content = 'hello, World'

p = re.compile(r'world', re.I)
rest = p.search(content)
print(rest)

rest_func = re.search(r'world', content, re.I);
print(rest_func)