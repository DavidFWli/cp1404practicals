import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUM_PICKS_PER_LINE = 6


def generate_quickly_picks(num_lines):
    quickly_picks = []
    for _ in range(num_lines):
        for _ in range(num_lines):
            pick = []
            while True:
                i = len(pick)
                a_num = random.randint(MIN_NUMBER, MAX_NUMBER + 1)
                if a_num in pick:
                    continue
                else:
                    if i < NUM_PICKS_PER_LINE:
                        pick.append(a_num)
                    else:
                        break
            pick.sort()
            quickly_picks.append(pick)

        return quickly_picks


def display_quickly_picks(quickly_picks):
    for pick in quickly_picks:
        # Format the numbers to align neatly
        formatted_pick = ' '.join(f"{num:>3}" for num in pick)
        print(formatted_pick)


# Main program
num_quick_picks = int(input("How many quick picks? "))
quickly_picks = generate_quickly_picks(num_quick_picks)
display_quickly_picks(quickly_picks)

