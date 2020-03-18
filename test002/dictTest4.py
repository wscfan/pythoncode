h1 = hash("abc")
print(h1)
h2 = hash("abc")
print(h2)
source = "123,aaa,ddd,5000$455,bbb,fff,4500$678,jjd,ret,4000"
sourceList = source.split("$")
print(sourceList)
tempObj = {}
for i in range(0, len(sourceList)):
    e = sourceList[i].split(",")
    print(e)
    emp = {
        "name": e[0],
        "age": e[1],
        "ins": e[2],
        "salary": e[3]
    }
    tempObj[emp['name']] = emp
print(tempObj)
infoInput = input("请输入编号:")
if infoInput in tempObj:
    tmpInfo = tempObj.get(infoInput)
    print("编号:{name},年龄：{age},兴趣：{ins}, 薪资：{salary}".format_map(tmpInfo))
else:
    print("员工信息不存在")
