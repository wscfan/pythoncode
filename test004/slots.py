class Student:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age

stu = Student('王大锤', 20)
# stu.sex = '男'