"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

again_or_not = 0
while again_or_not >=0 :
    score = float(input("Enter score: "))
    if score < 0:
        print("Invalid score")
    else:
        if score > 100:
            print("Invalid score")
        elif score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Passable")
        else :
            print("Bad")
    print("Do you want continue? If you want continue press 0, if not press -1")
    again_or_not = float(input())
print("Thank you.")