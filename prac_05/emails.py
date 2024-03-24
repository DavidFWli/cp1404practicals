def extract_name_from_email(email):
    parts = email.split('@')
    if len(parts) == 2:
        name = parts[0].split('.')
        return ' '.join(part.title() for part in name).strip()
    return None


def get_user_input():
    email_dict = {}
    while True:
        email = input("Email: ")
        if not email:
            break

        extracted_name = extract_name_from_email(email)
        if extracted_name is None:
            print("invalid email address")
            continue
        print("Is your name", extracted_name, "? (Y/n)")
        choice = input().lower()

        if choice == 'y' or choice == '':
            email_dict[email] = extracted_name
        else:
            name = input("Name: ")
            email_dict[email] = name

    return email_dict


def print_email_names(email_dict):
    for email, name in email_dict.items():
        print(name, "(", email, ")")


email_dict = get_user_input()
print_email_names(email_dict)