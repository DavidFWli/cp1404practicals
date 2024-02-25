import score


def main():
    grade = 0
    menus = """
        (G)et a valid grade 
        (P)rint result 
        (S)how stars 
        (Q)uit
    """
    while True:
        print(menus)
        choice = input(">>> ").upper()
        if choice == "Q":
            print("Bye!")
            return
        elif choice == "G":
            grade = float(input("Enter your grade (must be 0-100 inclusive): "))
        elif choice == "P":
            score.check_score(grade)
        elif choice == "S":
            show_stars(grade)


def show_stars(grade):
    if grade >= 90:
        print("****")
    elif grade >= 50:
        print("***")
    else:
        print("*")


main()
