import re

s = 'one1two2three334four4five5six6'
p = re.compile(r'\d+')
rest = p.split(s)
print(rest)