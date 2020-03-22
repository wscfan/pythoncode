l = ['a', 'b', 'c']
t = ('d', 'e', 'f')
s = 'abc123'
s2 = 'def,456'
r = range(1, 20)
print(list(t))
print(list(s))
print(s2.split(','))
print(list(r))
print('---------------------')
print(tuple(l))
print(tuple(s))
print(tuple(s2.split(',')))
print(tuple(r))
print('---------------------')
print(str(l))
print("".join(l))
print(str(t))
print(''.join(t))
print(str(r))
s3 = ''
for i in r:
    s3 += str(i)
print(s3)
