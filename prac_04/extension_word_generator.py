"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"


def is_valid_format(word_format):
    for char in word_format:
        if char not in "cv":
            return False
    return True


def generate_word(word_format):
    word = ""
    for char in word_format:
        if char == "c":
            word += random.choice(CONSONANTS)
        elif char == "v":
            word += random.choice(VOWELS)
    return word


def main():
    while True:
        # Get the word format from the user until a valid format is provided
        valid_format = False
        while not valid_format:
            user_format = input("Enter a valid word format (use 'c' for consonants, 'v' for vowels): ").lower()
            if is_valid_format(user_format):
                valid_format = True
            else:
                print("Invalid format. Please use only 'c' and 'v'.")

        # Generate and print the word
        word = generate_word(user_format)
        print(f"Generated word: {word}")

        # Ask if the user wants to continue
        if input("Do you want to generate another word? (y/n): ").lower() != "y":
            break


if __name__ == "__main__":
    main()