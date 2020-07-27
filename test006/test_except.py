def devide_num(num1, num2):
    try:
        return num1 / num2
    except (ZeroDivisionError, TypeError) as err:
        print("报错了")
        print(err)

if __name__ == '__main__':
    devide_num(5, 's')