def get_number(lower, upper):
    while True:
        try:
            number = int(input(f"Enter a number ({lower}-{upper}): "))
            if lower <= number <= upper:
                return number
            else:
                print("Please enter a number within the given range!")
        except ValueError:
            print("Please enter a valid number!")

# Test the function
try:
    number = get_number(10, 50)
    print(f"The number entered is: {number}")
except KeyboardInterrupt:
    print("Operation canceled by user.")