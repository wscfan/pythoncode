def main():
    try:
        with open('info.txt', 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print("无法打开指定的文件")
    except LookupError:
        print("指定了未知的编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误！")

if __name__ == '__main__':
    main()
