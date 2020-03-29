def calc(a, b, c):
    return a + b + c
l = [12, 23, 34]
print(calc(*l))
def personInfo(name, age, job):
    print(name)
    print(age)
    print(job)
dict = {"name": "张三", "age": 29, "job": "wenzhi"}
personInfo(**dict)