"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        if result != 0:
            print(result)
        else:
            print(result)
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)

