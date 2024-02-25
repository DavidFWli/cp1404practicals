"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    grade = float(input("Enter grade: "))
    check_score(grade)


def check_score(grade):
    if grade < 0 or grade > 100:
        print("Invalid score")
    elif grade >= 90:
        print("Excellent")
    elif grade >= 50:
        print("Passable")
    else:
        print("Bad")


main()
