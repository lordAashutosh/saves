#opp ==> object oriented programming
#==>two main point in the oop
# class  ==>person==>blueprint/ template
# object ==>ram ==> acutual instance of class




# class DateTime: # conciension ho ==> class= upper case and function ==> is in lower case 
#     def today_date(): # lower case ==> snakecase 
#         pass
#     def today_time():
#         pass
#     def today_day():
#         pass
#     def today_week():
#         pass
#     def today_month():
#         pass

# class Person:#frist latter sadai capital lekhyo vani developer haru le bujxan
#     name="ram"
#     age=22
#     address="ktm"

# ram = Person()
# print(ram)
# sita = Person()
# print(sita)


# class Person:#frist latter sadai capital lekhyo vani developer haru le bujxan
#     name="ram"
#     age=22
#     address="ktm"
#     # action / behaviours/ method
#     def eat():
#         pass
#     def walk():
#         pass
#     def sleep():
#         pass

# p1 = Person()
# print(p1.name)
# # print(p1.contanct) # navako chijj magye paxi error aauxa 
# p2 = Person()
# print(p2.name)
# def person(name,age,address):
#     print(name,age,address)

# person("aashutosh",17,"ktm")



# class Person1:
#     # aagadi paxadi double underscore ho 
#     def __init__(self,name,age,address):
#         print(name,age,address)

#     # attribute / property
#     # name ="Ram"
#     # age = 22 
#     # address = "bkt"
#     #ACTION / BEHAVIOURS / METHOD
#     def eat(self):
#         print("Eating")
#     def walk(self):
#         print("walking")
#     def sleep(self):
#         print("sleeping")


# p1 = Person1("nishana ",17,"ktm")
# print(p1.name) # value pass gareko vayera matra class run vako ho 
# but yesma value assign na vako vayera error aako 




# class Person1:
#     # aagadi paxadi double underscore ho ==>initializer==>constructer
#     def __init__(self,name,age,address):
#         # print(name,age,address)

#     #attribute / property
#         self.name =name
#         self.age = age
#         self.address = address
#     #ACTION / BEHAVIOURS / METHOD
#     def eat(self):
#         print("Eating")
#     def walk(self):
#         print("walking")
#     def sleep(self):
#         print("sleeping")


# p1 = Person1("nishana ",17,"ktm")
# print(p1.name)
# p2 = Person("Aashutosh",17,"bkt")
# print(p2.name)


# class Student:
#     def __init__(self,name,age,address,college,faculty,roll_no):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.college = college
#         self.facluty = faculty
#         self.roll_no = roll_no


#     def learn(self):
#         print(f"{self.name} is learning")


# s1 = Student(name="ram",age=23,address="ktm",college="nobel academy",faculty="science",roll_no=1)
# s1.learn()


# to make an edit as user 
# making above program dyanmic 

# class Student:
#     def __init__(self,name,age,address,college,faculty,roll_no):
#         self.name = name
#         self.age = age
#         self.address = address
#         self.college = college
#         self.facluty = faculty
#         self.roll_no = roll_no
#         self.subject = []
#     def add_new_subject(self, subject_name):
#         self.subject.append(subject_name)


#     def learn(self):
#         print(f"{self.name} is learning")


# s1 = Student(name="ram",age=23,address="ktm",college="nobel academy",faculty="science",roll_no=1)
# print(s1.subject)
# s1.add_new_subject("python")
# print(s1.subject)
# s1.add_new_subject("Django")
# print(s1.subject)
# s1.add_new_subject("java")
# print(sorted(s1.subject))# making in  proper arangement usig sorted 







# class Rectangle:
#     def __init__(self,lenght,breadth):
#         self.l=lenght
#         self.b=breadth
#     #public method
#     def area(self):
#         return self.l * self.b
#     #public method
#     def perimetere(self):
#         return 2*(self.l*self.b)
#     def lenght_getter(self):
#         return
    
# r1 = Rectangle(4,30)
# print(r1.area())
# print(r1.perimetere())
# r1 = lenght_getter()
# print(r1.perimetere())



 ### ENCAPSULATION ==> acess modifier ==> public , private , protected

#     def __init__(self,lenght,breadth):
#         self.__l=lenght
#         self.__b=breadth
#     
# #private attributes/private methods
#     def area(self):
#         return self.__l * self.__b
#    private attributes/private methods
#     def perimetere(self):
#         return 2*(self.__l*self.__b)
    
# r1 = Rectangle(4,44)
# print(r1.area())
# print(r1.perimetere())
# """


# from math import pi

# class Cirlce:
#     def __init__(self,r):
#         self.r = r

#     def area(self):
#         return pi *self.r**2
#     def perimeter(self):
#         return 2*pi*self.r
# c1 = Cirlce(5)
# print(c1.area)
# print(c1.perimeter)


# it  can identify the data type and give boolean value 
# print(isinstance( 1,int))
# print(isinstance( 1,(int,float)))
 



class rectangle:
    def __init__(self,lenght,breadth):
        self.__l=lenght
        self.__b=breadth
    #public method
    def area(self):
        return self.__l * self.__b
    def perimeter(self):
        return 2*(self.__l*self.__b)
    def lenght_getter(self):
        return self.__l
    def lenght_setter(self,value):
        if isinstance(value,(int,float)):
            self.__l = value
        else:
            raise TypeError("value must be int or float")    
 

r1  = rectangle(4,5)
# answer = int(input("enter 1 for area and 2 for perimeter\n"))
print(r1.lenght_setter(1))
print(r1.lenght_getter())





class BankAccount:
    def __init__(self,balance=0):
        self.__balance = balance #private atribute
    def deposit(self,amount):
       if amount > 0:
            self.__balance += amount
            print(f"deposited :{amount}")
       else:
           print("invalid amount")or print("deposited amount must be positive")
    def withdraw(self,amount):
       if 0<amount<=self.__balance:
           self.__balance -= amount
           print(f"withdraw :{amount}")
       else:
           print("insufficient balance")

    def get_balance(self):
        return self.__balance # public method to access private attribute
    
    #usage 
account=BankAccount()
account.deposit(100)
account.withdraw(50)
print(f"Balance: {account.get_balance()}")#accessing balance via public method
    # account.__balance = 1000 # raises attribute Error, can't modify directly

     



class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

p = Point(1,2)
print(p) #==> to make answer (1,2)



class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"
    
p = Point(1,2)
print(p)



# p1 = point(1,2)
# p2 = point(2,2)
# p1 + p2#==> to make answer (3,4)

class point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x},{self.y})"
    def __repr__(self):
        return f"point({self.x},{self.y})"
    def __add__(self, other):
        total_x = self.x + other.x
        total_y = self.y + other.y
        return point(total_x,total_y)

p1 = point(1,2)
p2 = point(2,2)
p3 = p1 + p2
print(p3)


