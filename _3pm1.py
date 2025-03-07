def odd_or_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
    
result = odd_or_even(1)
print(result)
# both code is correct and same but 1 line is skip .
def odd_or_even(number):
    if number%2==0:
        return "even"
    return "odd"

results = odd_or_even(10)
print(results)
def greet_user(name,address,country):
    print(f"{name} comes from {country} and they live in {address}")
# greet_user("ktm","sushan","nepal") # positional argument
greet_user(country="nepal",address="ktm",name="suahn")



# def make_user_details_better(name,address,country):
#     name = name.title()
#     address = address.strip()
#     country = country.upper()
#     return name, address, country

# print(make_user_details_better("sushant,"ktm","nepal"))
# from random import randint
# def game_play():
#     MIN_NUMBER = 1
#     MAX_NUMBER = 100
#     random_number = randint(MIN_NUMBER,MAX_NUMBER)
#     ATTEMPTS = 5
#     while True:
#         user_guess = int(input("enter your no\n"))#assuming that user will input integer
#         if user_guess == random_number:
#             print("you won")
#             break
#         ATTEMPTS=ATTEMPTS-1
#         if ATTEMPTS == 0:
#             print("you lost")
#             break

from random import randint

def game_play():
    MIN_NUMBER = 1
    MAX_NUMBER = 100
    random_number = randint(MIN_NUMBER, MAX_NUMBER)
    ATTEMPTS = 5
    
    while ATTEMPTS > 0:
        try:
            user_guess = int(input(f"Enter your guess ({MIN_NUMBER}-{MAX_NUMBER}): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # Skip the rest of the loop and ask again

        if user_guess == random_number:
            print("You won!")
            break
        elif user_guess < random_number:
            print("Too low!")
        else:
            print("Too high!")
        
        ATTEMPTS -= 1
        if ATTEMPTS > 0:
            print(f"You have {ATTEMPTS} attempts left.")
        else:
            print(f"You lost! The correct number was {random_number}.")

# Call the function to start the game
game_play()




# def adder(*agrs):
#     sum = 0
#     for each_no in agrs:
#         sum = sum + each_no
#     print(sum)

# adder(5,10,520,510,510,10,20,30,40,50)



# def make_word_uppercase(*agrs):
#     for each_word in agrs:
#         a = each_word.upper
#     print(a)

# make_word_uppercase("aashutosh","sukuna","aizen")
# def make_uppercase(*args):
#     uppercased_word = ""
#     for each in args:
#         uppercased_word = uppercased_word + each.upper()
#     print(uppercased_word)
 
# make_uppercase('arjun', 'ram', 'hari', 'shyam')