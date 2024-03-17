"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

print(CODE_TO_NAME)

while True:
    state_code = input("Enter short state (or leave blank to exit): ").upper()
    if not state_code:
        break
    try:
        print(f"{state_code.upper()} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")

# Print all states and names neatly aligned
for code, name in CODE_TO_NAME.items():
    print(f"{code.upper()}\t is {name}")