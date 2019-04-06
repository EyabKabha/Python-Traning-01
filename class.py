class Animal():
    
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def eat(self):
        print("I am a dog and eating")
    def bark(self):
       print("WOOF!!")

mydog=Dog()    # --> Animal Created ,  Dog Created
mydog.eat()    # --> I am a dog and eating
mydog.bark()   #-->  WOOF!!

# self -  Keyword it represents the instance of the object it self.