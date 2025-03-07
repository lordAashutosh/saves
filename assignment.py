#create a class called father 
#create a class called son which 

# class Father:
#     def __init__(self):
#         print("father")

#     def bank_balance(self):
#         print("100")

#     def habbit(self):
#         print("exercise,jogging , reading ,watching tv")
class Person:
    def __init__(self, name, address, age):
        self.__name = name
        self.address = address
        self.age = age

    def display_info(self):
        print(f"Name: {self.__name}")
        print(f"Address: {self.address}")
        print(f"Age: {self.age}")


person = Person("John Doe", "123 Main St", 30)
person.display_info()