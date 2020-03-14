while(True):
    inputNum = input("请输入需要测试的数字：")
    if (int(inputNum) > 60 and int(inputNum) < 90):
        print("测试成功")
        break
    else:
        print("测试失败")