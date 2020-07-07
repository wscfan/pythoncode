class Cat(object):
    speak = "喵喵"
    @staticmethod
    def breath():
        print("猫需要呼吸")

    @classmethod
    def speaking(cls):
        print(cls.speak)

if __name__ == '__main__':
    Cat.breath()
    cat1 = Cat()
    cat1.speaking()
    Cat.speaking()