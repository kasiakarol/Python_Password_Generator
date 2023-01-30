import random
from Clear_function import clear

another_password = True

# Printing the rules
print("Welcome to the Password Generator Program!")
print("The total number of characters in your password will consists of: \n- letters, \n- symbols, \n- numbers.\n")

while another_password:
    # List of the allowed signs
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    # Asking the user for the input
    try:
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input("How many symbols would you like?\n"))
        nr_numbers = int(input("How many numbers would you like?\n"))

        password = ""

        for letter in range(1, nr_letters+1):
            password += random.choice(letters)

        for symbol in range(1, nr_symbols+1):
            password += random.choice(symbols)

        for number in range(1, nr_numbers+1):
            password += random.choice(numbers)

        # Mixing up the characters to increase the password's complexity
        password_random = ''.join(random.sample(password, len(password)))

        print(f"Your password is: {password_random}\n")

        another_pwd_input = input("Would you like to generate another password? Y/N: ")

        if another_pwd_input.upper() == "N":
            another_password = False
        elif another_pwd_input.upper() == "Y":
            another_password = True
            clear()
        else:
            print("Incorrect input.")
            another_password = False

    except:
        print("Incorrect input! Please try again with the correct values.\n")

