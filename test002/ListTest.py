aa = ["张三", "李四", "王五", "赵六"]
aa.reverse()
print(aa)
aa.sort()
print(aa)
aa.sort(reverse=True)
print(aa)
aa.append("aaaa")
print(aa)
aa.insert(0, "-1")
print(aa)
aa[0] = "大王"
print(aa)
aa.remove("aaaa")
print(aa)
aa.pop()
print(aa)
print(aa.count("李四"))
aa.append(["京山", "银山"])
print(aa)
aa.extend(["北京", "上海"])
print(aa)
print("上海" in aa)
bb = aa.copy()
print(bb)
print(aa is bb)
bb.clear()
print(bb)
