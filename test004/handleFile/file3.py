import time

def main():
    try:
        with open('info.txt', 'r', encoding='utf-8') as f:
            for line in f:
                print(line, end='')
                time.sleep(0.5)
    except FileNotFoundError:
        print("无法打开指定的文件")
    except LookupError:
        print("指定了未知的编码")
    except UnicodeDecodeError:
        print("读取文件时解码错误！")

if __name__ == '__main__':
    main()
