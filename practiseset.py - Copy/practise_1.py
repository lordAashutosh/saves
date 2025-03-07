# from now , aafai pythoon pracrise garxu , 

    # # safe password generator for the user
import random
import string

def generate_password(length=12):
    # Define the characters to use in the password
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly choose characters from the set
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password

# Example usage:
password = generate_password(16)  # Generates a password of length 16
print("Generated Password:", password)
