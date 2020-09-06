import sys

l = []
l2 = l
l3 = l
print(sys.getrefcount(l))
del l3
print(sys.getrefcount(l))