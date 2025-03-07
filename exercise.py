# write a program for user to enter their details about
# their name, salary,address, department
#define a function which take department and salary as an argument
# and lets you known if that is a valid salary range

print("**check fairness***")

def get_user_info():
    name = input("enter a your name\n")
    salary = float(input("enter your salary\n"))
    department = input("enter your department\n")
    return name,salary,department


def is_fair_salary(salary, department):
    if department == "admin" and salary > 500:
        return True
    if department == "it" and salary > 100:
        return True
    if department == "cook" and salary > 200:
        return False
    

name, salary, department = get_user_info() # tuple unpacking
result = is_fair_salary(salary, department)
if result == True:
    print(f"wow{name}, your salary is fair")
else:
    print(" be gratefull")
    



    # take input form a user min and max range 
    # write a function which takes min and max range
    # if min and max ramge is not provided give default value of 1 and 3 respectivrly
    #generate a random number between min and max range
    #retuen the random random number 
    # check if that random number is 5 , if yess say"user won the game"
    #else "you lost"

    #user givee me minimun range 
    #5
    # user give me maximum range
    #5
    #user give a minimm range 
    #10
    #result = your_function(minimum, maximum)
    #if result==5:
    #user won the game
    #else:
def generate_random_no(lowest_range, highest_range):
    from random import randint
    result = randint(lowest_range,highest_range)

lowest_range = int(input("user -- Enter a lowest range to generate\n"))
highest_range = int(input("user-- Enter a highest range to generate random number\n"))

result = generate_random_no(lowest_range, highest_range)
a = int(input("User- Enter a integer number as ur guesss")) # asking user a guess no 
if result == a:
    print("you- won")
else:
    print("you lost")
    
