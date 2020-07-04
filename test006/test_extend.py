class Animal(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def tell(self):
        print("我叫{0},我今天{1}岁了".format(self.__name, self.__age))

class Dog(Animal):
    pass

class Cat(Animal):
    pass

if __name__ == "__main__":
    print(issubclass(Dog, Animal))