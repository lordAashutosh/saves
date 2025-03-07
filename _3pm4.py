# start from 19 november
# TaBNIne 
# codeium
# class Dog:
#     def __init__(self,name):
#         self.name = name
#     def bark(self):
#         print(f"{self.name} barks!")

#     def __str__(self):
#         return self.name# magic method , or dunder method
    

# dog1 = Dog('bruno')
# print(dog1)

# # print(len(dog1))




# class Container:
#     def __init__(self,item):
#         self.item = item.split(",")
    


#     def display_items(self):
#         print("".join(self.items))


# china_to_us_container = Container("iphone,charger,headphone")# insntance /object 
# nepal_to_us_container = Container("carpet,hancraft item, pasmina")
# tezaistan_to_vietnam_container = Container("carrot,cofee,butter")



# print(len(tezaistan_to_vietnam_container))


USERS = []

class User:
    def __init__(self,name,password, email, phone = None):
        from random import randint
        # this id may already exist (we will create a new id if exist)
        self.id = randint(1,1000)
        self.first_name = name.split(" ")[0]
        self.last_name = name.split(" ")[1]
        self.password = password + "_secret" #hasing
        self.email = email
        self.phone = phone

        user_data = {
            "id ":self.id,
            "first_name":self.last_name,
            "password":self.password,
            "email":self.email,
            "phone":self.phone

        }
        USERS.append(user_data)


    def __str__(self):
        return f"{self.first_name} { self.last_name}"
    

Bishnu = User("Bishnu Khatri","bishnu123", "bishnuk@gmail.com")

