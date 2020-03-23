s1 = {1, 2, 3, 4}
s2 = {1, 2, 3, 4}
s3 = {1, 2, 3, 4, 5, 6}
print(s1 == s2)
print(s2.issubset(s3))
print(s3.issuperset(s2))
print(s2.isdisjoint(s3))