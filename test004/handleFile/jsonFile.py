import json

def main():
    mydict = {
        'name': '张三',
        'age': 24,
        'friends': [
            {'name': '李四', 'age': 24},
            {'name': '王五', 'age': 22}
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print("数据保存完成")

if __name__ == '__main__':
    main()