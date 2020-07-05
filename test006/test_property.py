class PetCat(object):
    """家猫"""
    def __init__(self, name, age):
        """
        构造方法
        :param name: 猫的名称
        :param age: 猫的年龄
        """
        self.name = name
        self.__age = age

    def __str__(self):
        return self.show_info

    @property
    def show_info(self):
        """显示猫的信息"""
        return '我叫{0}，今年{1}岁了'.format(self.name, self.__age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            print("年龄需要为整数")
            return 0
        if age < 0 or age > 100:
            print("年龄范围不对")
            return 0

        self.__age = age

if __name__ == '__main__':
    cat = PetCat('小黑', 2)
    rest = cat.show_info
    print(rest)
    print(cat)
    print(cat.age)
    cat.age = 99
    print(cat.age)