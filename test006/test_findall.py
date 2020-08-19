import re

content = 'one1tow22Three333four4444five5six6'

p = re.compile(r'\d+')

rest = p.findall(content)
print(rest)

all_rest = re.findall(r'[a-z]+', content, re.I)
print(all_rest)