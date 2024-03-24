MENU = """
    (H)ello
    (G)oodbye
    (Q)uit
"""

while True:
    print(MENU)
    choice = input(">>> ").upper()
    if choice == "H":   
        print("Hello Guido")
    elif choice == "G":
        print("Goodbye Guido")
    elif choice == "Q":
        print("Finished.")
        break
    else:
        print("Invalid option")
