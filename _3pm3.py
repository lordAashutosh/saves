# oop==> object oriented programming
# -->different  paradigm than structural
#-->polymorphism, encapsulation , abstraction, inheritances --> pillars 
# class ClassName:
#     def __init__(self):
#         pass
#     def method(self):
#         pass

# obj1 = ClassName()
# obj1 = ClassName()
# from random import randint
# randint(1,10)# funtion

# abc = "aashutosh"
# abc.upper()


class Dog:
    def __init__(self,name):
        self.name = name
    def bark(self): # method for object
        print(f"{self.name} is barking")


dog1 = Dog("jackie")  # object
dog1.bark()
dog2 = Dog("bruno") # object
dog2.bark()

# maagic method    





# new 
class Product:
    def __init__(self,name,price,):
        print("ma init method hora ma run vae")
        self.name = name
        self.price = price
        self.discount = 0


    def display_product(self):
        print("ma display prodect ho ra ma run vae")
        print(f"Name:{self.name}")

laptop = Product("laptop" , 1000)
laptop.display_product()



# assigment --> crete a class name calculator , which takes num1 and num 2 as arugement 
# define 4 method, add , subrtact ,m multiply , and division
# all method should called by object and print the result

# class Calculator:
#     def __init__(self,add,subtract,multipy,division):
#         self.add = add
#         self.subtract = subtract
#         self.multiply = multipy
#         self.division = division


#     def addition(self):
#         print("the sum is :num1 + num2")
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        print(f"The addition result is: {result}")

    def subtract(self):
        result = self.num1 - self.num2
        print(f"The subtraction result is: {result}")

    def multiply(self):
        result = self.num1 * self.num2
        print(f"The multiplication result is: {result}")

    def divide(self):
        
            result = self.num1 / self.num2
            print(f"The division result is: {result}")
       

# Create an object of the Calculator class
calc = Calculator(10, 2)

# Calling methods using the object
calc.add()
calc.subtract()
calc.multiply()
calc.divide()











# class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        result = self.num1 + self.num2
        print(f"The addition result is: {result}")

    def subtract(self):
        result = self.num1 - self.num2
        print(f"The subtraction result is: {result}")

    def multiply(self):
        result = self.num1 * self.num2
        print(f"The multiplication result is: {result}")

    def divide(self):
        if self.num2 != 0:
            result = self.num1 / self.num2
            print(f"The division result is: {result}")
        else:
            print("Error: Division by zero is not allowed.")

# Create an object of the Calculator class
calc = Calculator(10, 5)

# Calling methods using the object
calc.add()
calc.subtract()
calc.multiply()
calc.divide()





        

