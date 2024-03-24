"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer:data type mismatch, Too many or too few parameters, Incorrect file format, Number overflow, Immutable object
2. When will a ZeroDivisionError occur?
Answer: This is caused by a divisor of 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    if denominator != 0:
        fraction = numerator / denominator
        print(fraction)
    else:
        print("The denominator cannot be zero!")
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")