"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing", "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)  # Output: ['B', 'A', 'J', 'A', 'A']

# list comprehension that does the same thing as the loop above
first_initials = [name[0] for name in names]
print(first_initials)  # Output: ['B', 'A', 'J', 'A', 'A']

# list comprehension that creates a list containing the initials
# this splits each name and adds the first letters of each part to a string
full_initials = [name.split()[0][0] + name.split()[1][0] for name in full_names]
print(full_initials)  # Output: ['BM', 'AH', 'JH', 'AT', 'AL']

# this example uses filtering to select only the names that start with A
a_names = [name for name in names if name.startswith('A')]
print(a_names)  # Output: ['Ada']

# and here's the join string method being used to create a single string from the names like:
# 'Ada Alan Angel Bob Jimi'
print(" ".join(sorted(names)))  # Output: 'Ada Angel Bob Jimi Alan'

# TODO: list comprehension to create a list of all the full_names in lowercase format
# lowercase_full_names =
lowercase_full_names = [full_name.lower() for full_name in full_names]
print(lowercase_full_names)  # Output: ['bob martin', 'angel harlem', 'jimi hendrix', 'alan turing', 'ada lovelace']

# TODO: list comprehension to create a list of integers from the above list of strings
# numbers =
almost_numbers = ['0', '10', '21', '3', '-7', '88', '9']
numbers = [int(num) for num in almost_numbers]
print(numbers)  # Output: [0, 10, 21, 3, -7, 88, 9]

# TODO: list comprehension to create a list of only the numbers that are
# greater than 9 from the numbers (not strings) you just created
greater_than_9 = [num for num in numbers if num > 9]
print(greater_than_9)  # Output: [10, 21, 88]

# TODO: (more advanced) use a list comprehension and the join string method
# to create a string (not list) of the last names for those full names longer than 11 characters
# the result should be: 'Harlem, Hendrix, Lovelace'
long_names = [full_name.split()[-1] for full_name in full_names if len(full_name) > 11]
long_names_string = ", ".join(long_names)
print(long_names_string)  # Output: 'Harlem, Hendrix, Lovelace'
