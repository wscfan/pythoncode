totalList = []
while True:
    inputStr = input("请输入人员列表")
    if inputStr == '':
        break
    inputArr = inputStr.split(",")
    totalList.extend(inputArr)
    print(totalList)
