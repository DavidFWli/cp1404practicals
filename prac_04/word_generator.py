"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"
ALL_LETTERS = VOWELS + CONSONANTS


def generate_word(word_format):
    word = ""
    for char in word_format:
        if char == "#":
            word += random.choice(VOWELS)
        elif char == "%":
            word += random.choice(CONSONANTS)
        elif char == "*":
            word += random.choice(ALL_LETTERS)
        else:
            word += char
    return word


def main():
    while True:
        # Get the word format from the user
        user_format = input(
            "Enter a word format (use # for vowels, % for consonants, * for any letter, or a specific letter): ").lower()

        # Optionally, automatically generate the word format
        if input("Do you want to generate a random word format? (y/n): ").lower() == "y":
            random_format = ''.join(random.choices("#%", k=random.randint(3, 8)))
            user_format = random_format

        # Generate and print the word
        word = generate_word(user_format)
        print(f"Generated word: {word}")

        # Ask if the user wants to continue
        if input("Do you want to generate another word? (y/n): ").lower() != "y":
            break


if __name__ == "__main__":
    main()