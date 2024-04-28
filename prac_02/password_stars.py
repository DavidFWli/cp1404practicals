def main():
    get_password()


def get_password():
    pwd = input("Please enter you password (at least 8 chars): ")
    length = len(pwd)
    if length >= 8:
        print("Here is your password:")
        print("*" * length)
    else:
        print("Invalid password")


if __name__ == '__main__':
    main()
