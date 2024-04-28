class Guitar:
    def __init__(self, name="", year=0, cost=0.0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def get_age(self, current_year=2022):
        return current_year - self.year

    def is_vintage(self, current_year=2022):
        return self.get_age(current_year) >= 50


# Creating a guitar instance
my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)

# Printing the guitar
print(my_guitar)

# Getting the age of the guitar
age = my_guitar.get_age()
print(f"Age: {age} years")

# Checking if the guitar is vintage
is_vintage = my_guitar.is_vintage()
print(f"Is vintage: {is_vintage}")
