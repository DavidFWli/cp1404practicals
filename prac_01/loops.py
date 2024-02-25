MENU = """
    A - count in 10s from 0 to 100
    B - count down from 20 to 1
    C - Ask for a number, then print that many stars (*)
    D - print n lines of increasing stars
    Q - Quit
"""
while True:
    print(MENU)
    choice = input(">>> ").upper()
    if choice == "A":
        for i in range(0, 100+1, 10):
            print(i, end=' ')
        print()
    elif choice == "B":
        for i in range(20, 0, -1):
            print(i, end=' ')
        print()
    elif choice == "C":
        star= int(input("Please enter the number of star: ")) 
        for i in range(0,star):
            print("*",end="")
        print()
    elif choice == "D":
        line= int(input("Please enter the number of lines(stars): "))
        for i in range(0,line+1,1):
            for j in range(0,i):
                print("*",end='')
            print()
        print()
    elif choice == "Q":
        print("Thank you.")
        break
    else:
        print("Invalid option")
