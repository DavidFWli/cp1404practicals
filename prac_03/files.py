with open('name.txt', 'w') as f:
    name = input("please enter your name:")
    f.write('My name is ' + str(name))

with open("name.txt", "r") as file:
    line = file.readline()
    print(line.strip())


with open("numbers.txt", "r") as file:
    lines = file.readlines()
    if len(lines) < 2:
        print("least 2 lines.")
    else:
        # Strip removes leading and trailing spaces, split splits strings into lists based on spaces
        line_one = lines[0].strip().split()
        line_two = lines[1].strip().split()

    # Convert to integers and add them up
    result = [str(int(a) + int(b)) for a, b in zip(line_one, line_two)]

    # Connect elements in the result list with spaces and print
    print(' '.join(result))

with open("numbers.txt", "r") as file:
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        print(lines[i])