# # IN THIS , I WILL TRY TO DEVELOP A ADVANCE GAME OF GUESSING NUMBER WHICH INSIST MANY ROUND
# import random

# def play_game(round_range):
#     number = random.randint(1, round_range)
#     attempts = 5
    
#     print(f"\nGuess the number between 1 and {round_range}:")
    
#     for attempt in range(1, attempts + 1):xxxxxxxxx
#         guess = int(input(f"Attempt {attempt}: "))
        
#         if guess == number:
#             print("Congratulations! You've guessed the correct number!")
#             return True
#         elif guess < number:
#             print("Too low! Try again.")
#         else:
#             print("Too high! Try again.")
    
#     print(f"Sorry, you've used all {attempts} attempts. The correct number was {number}.")
#     return False

# def main():
#     print("Welcome to the Number Guessing Game!")
    
#     rounds = [10, 100, 100]  # Ranges for the three rounds
    
#     for i, round_range in enumerate(rounds, start=1):
#         print(f"\nRound {i}:")
#         if not play_game(round_range):
#             break
    
#     print("\nGame Over!")
#     restart = input("Do you want to play again? (yes/no): ").strip().lower()
#     if restart == "yes":
#         main()
#     else:
#         print("Thanks for playing!")

# if __name__ == "__main__":
#     main()
import random  # Import the random module to generate random numbers

def play_game(round_range):
    number = random.randint(1, round_range)  # Generate a random number within the given range
    attempts = 5  # Number of attempts allowed
    
    print(f"\nGuess the number between 1 and {round_range}:")
    # a = number + 100
    # print(a)

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: "))  # Prompt the player to guess the number
        if attempt == 4:
            b = (number + number)/2
            print(f"this is hint for u , the mid value of number is {b}. hope this  will help u to solve this puzzle")
     
        if guess == number:
            print("Congratulations! You've guessed the correct number!")  # Player guessed correctly
            return True
        elif guess < number:
            print("Too low! Try again.")  # Guess was too low
        else:
            print("Too high! Try again.")  # Guess was too high
    
    print(f"Sorry, you've used all {attempts} attempts. The correct number was {number}.")
    return False  # Player did not guess correctly within the given attempts

def main():
    print("Welcome to the Number Guessing Game!")
    
    rounds = [10, 100, 1000]  # Ranges for the three rounds
    
    # Loop through each round
    for i, round_range in enumerate(rounds, start=1):
        print(f"\nRound {i}:")
        if not play_game(round_range):
            break  # Exit if the player fails a round
    
    print("\nGame Over!")
    restart = input("Do you want to play again? (yes/no): ").strip().lower()  # Prompt to restart the game
    if restart == "yes":
        main()  # Restart the game
    else:
        print("Thanks for playing!")  # Exit message

if __name__ == "__main__":
    main()  # Start the game

