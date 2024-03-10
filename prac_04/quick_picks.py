import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_PICKS_PER_LINE = 6


def generate_quick_picks(num_lines):
    quick_picks = []

    for _ in range(num_lines):
        # Generate a list of numbers from 1 to 45
        numbers = list(range(MIN_NUMBER, MAX_NUMBER + 1))

        # Shuffle the list of numbers
        random.shuffle(numbers)

        # Take the first 6 numbers from the shuffled list
        pick = numbers[:NUM_PICKS_PER_LINE]

        # Sort the numbers in ascending order
        pick.sort()

        # Append the pick to the list of quick picks
        quick_picks.append(pick)

    return quick_picks


def display_quick_picks(quick_picks):
    for pick in quick_picks:
        # Format the numbers to align neatly
        formatted_pick = ' '.join(f"{num:2}" for num in pick)
        print(formatted_pick)


# Main program
num_quick_picks = int(input("How many quick picks? "))
quick_picks = generate_quick_picks(num_quick_picks)
display_quick_picks(quick_picks)
