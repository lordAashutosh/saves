def count_character_frequency(input_string):
    # Initialize an empty dictionary to store the character frequencies
    frequency_dict = {}

    # Process the string: remove spaces and convert to lowercase
    processed_string = input_string.replace(" ", "").lower()

    # Count the frequency of each character
    for char in processed_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1

    return frequency_dict

# Get input from the user
user_input = input("Enter a string: ")

# Get the frequency dictionary
result = count_character_frequency(user_input)

# Print the result
print("Character frequencies (ignoring spaces and case):")
print(result)

# def count_character_frequency(input_string):
  
#     frequency = {}
#     for char in input_string:
#         char = char.lower()
#         if char != " ": # ignore the space
#             if char in frequency:
#                 frequency[char] += 1
#             else:
#                 frequency[char] = 1

#     return frequency

# user_input = input("Enter a string: ")
# result = count_character_frequency(user_input)
# print("Character frequencies (by ignoring spaces and cases):")
# print(result)
