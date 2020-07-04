class Animal(object):
    def eat(self):
        print('eat............')

class Thing(object):
    def tellName(self):
        print('my..............')

class Dog(Animal, Thing):
    pass

if __name__ == "__main__":
    dog = Dog()
    dog.eat()
    dog.tellName()