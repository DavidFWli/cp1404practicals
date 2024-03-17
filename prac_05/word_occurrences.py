def count_words(string):
    """
    Count the occurrences of words in a string and format the output.

    Parameters:
    string (str): The input string containing the words.

    Returns:
    None (outputs the formatted result to the console).

    Time Estimate: O(n), where n is the number of characters in the string.
    """
    # Split the string into words
    words = string.split()

    # Initialize a dictionary to store word counts
    word_counts = {}

    # Iterate over the words and update their counts in the dictionary
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    # Find the longest word for formatting
    longest_word = max(word_counts, key=len)

    # Sort the words alphabetically
    sorted_words = sorted(word_counts)

    # Print the formatted word counts
    for word in sorted_words:
        count = word_counts[word]
        formatted_word = word.rjust(len(longest_word))  # Right-justify the word to match the longest word's length
        print(f"{formatted_word} : {count}")


# Get user input
user_string = input("Text: ")

# Count and print word occurrences
count_words(user_string)
