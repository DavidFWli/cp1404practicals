FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print("Data:")
    display_subject_details(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data_list = []
    with open(FILENAME, 'r') as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data_list.append(parts)
    return data_list


def display_subject_details(data):
    """Display subject details in a formatted way."""
    for subject, lecturer, num_students in data:
        print(f"{subject} is taught by {lecturer} and has {num_students} students")


main()
