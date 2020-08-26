import re

s = 'one1two2three334four4five5six6'
p = re.compile(r'\d+')
rest = p.sub('@', s)
print(rest)

s2 = 'hello world'
p2 = re.compile(r'(\w+) (\w+)')
rest = p2.sub(r'\2 \1', s2)
print(rest)

def f(m):
    return m.group(1).upper() + " " + m.group(2)
rest = p2.sub(f, s2)
print(rest)

print('---------------------')
rest = p2.sub(lambda m: m.group(1).upper() + ' ' + m.group(2), s2)
print(rest)