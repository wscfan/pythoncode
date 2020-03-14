"""
format测试
"""
name = "房子"
money = 123545.12312
str = "今天买{}花了￥{:0,.2f}元".format(name, money)
print(str)