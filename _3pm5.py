# class Father:
#     def __init__(self):
#         print("i am father of father") 

# class Mother:
#     def __init__(self):
#         pass

class Animal:
    def __init__(self,name ):
        self.name = name


    def eat(self):
        print(f"{self.name}is a eating ")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)


    def eat(self):
        print("ma khadai xu ")



animal1 = Animal("tiger")
animal2 = Animal("cat")
animal3 = Animal("dog")
dog = Dog("jackie")
dog.eat()


    