"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """
    C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit
"""


def main():
    calc_temperatures()


def calc_temperatures():
    print(MENU)
    choice = input(">>> ").upper()
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = (fahrenheit - 32) / 9.0 * 5
        print(f"Result: {celsius:.2f} C")
    elif choice == "Q":
        print("Thank you.")
    else:
        print("Invalid option")


main()
