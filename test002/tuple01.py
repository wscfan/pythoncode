t = ("张三", "李四", 'aaa')
print(t * 2)
t2 = 'a', 'b', 'c', 'd'
print(t2)
print(type(t2))
print(t2[2])
print(t2[-1])
print('a' in t2)
t3 = ([1, 2, 3], 'aaa', 'bbb')
t3[0][1] = 'a'
print(t3)
t3[0].append('dddd')
print(t3)
t4 = (1, 2, 3) + (4, 5, 6)
print(t4)
t5 = ('a', 'b', 'c') * 3
print(t5)
t6 = ('good!') * 4
print(t6)
