MENU = """
    C - Enter your password
    Q - Quit
"""

while True:
    print(MENU)
    choice = input(">>> ").upper()
    if choice == "C":
        length = len(input("Please enter you password: "))
        if length >= 8:
            print("Here is your password:")
            print("*"*length)
        else:
            print("Invalid password, please try again")
    elif choice == "Q":
        print("Thank you.")
        break
    else:
        print("Invalid option")