"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True # change it to True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)} character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    is_valid=False
    if MIN_LENGTH>len(password) or len(password)>MAX_LENGTH:
        return is_valid

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.isdigit():
            count_digit += 1
            print("1 digit")
        elif char.islower():
            count_lower += 1
            print("1 lower")
        elif char.isupper():
            count_upper += 1
            print("1 upper")
        elif char in SPECIAL_CHARACTERS:
            count_special += 1
            print("1 special")

    if count_lower >= 1 and count_digit >= 1 and count_upper >= 1:
        is_valid = True
    if SPECIAL_CHARS_REQUIRED:
        if count_special >= 1 and is_valid == True:
            is_valid = True
        else:
            is_valid = False

    # if we get here (without returning False), then the password must be valid
    return is_valid


main()
