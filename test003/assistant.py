import random

phone_number_str = "匪警[110],火警[119],急救中心[120]"
weather_str = "北京,2020年3月29日,多云,8℃,-4℃,南风3级~上海,2020年3月29日,晴,4℃,-6℃,南风5级"

# 双色球
def generate_unionlotto(number):
    for i in range(0, int(number)):
        for j in range(0, 6):
            red = random.randint(1, 33)
            print(red, end=' ')
        blue = random.randint(1, 16)
        print(blue)

# 号码百事通
def find_phone(number):
    phone_list = phone_number_str.split(",")
    for i in phone_list:
        if i.find(number) != -1:
            print(i)

# 天气查询
def get_weather(city):
    city_list = weather_str.split("~")
    weather_dict = {}
    for i in city_list:
        w = i.split(",")
        city_weather = {"name": w[0], "date": w[1], "weather": w[2], "max": w[3], "min": w[4], "wind": w[5]}
        weather_dict[city_weather["name"]] = city_weather
    if city in weather_dict:
        return weather_dict.get(city)
    else:
        return {}

while True:
    print("1-双色球随机数")
    print("2-号码百事通")
    print("3-明日天气预报")
    print("0-结束程序")
    c = input("请输入功能编号：")
    if c == "1":
        n = input("您要生成几注双色球号码：")
        generate_unionlotto(n)
    elif c == "2":
        n = input("请输入您要查询的机构或者电话号码：")
        find_phone(n)
    elif c == "3":
        city = input("请输入需要查询的城市：")
        weather_info = get_weather(city)
        if "name" in weather_info:
            print("{date} {name} {weather} {max}/{min} {wind}".format_map(weather_info))
        else:
            print("未找到{0}的天气数据".format(city))
    elif c == "0":
        break
    else:
        print('您输入的功能编号有误，请重新输入')
    print("============================")
print("感谢您的使用，祝您生活愉快，再见！")