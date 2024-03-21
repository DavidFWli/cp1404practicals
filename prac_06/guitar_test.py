# Import the Guitar class from the guitar module
from guitar import Guitar

# Create two guitar instances
gibson_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
another_guitar = Guitar("Another Guitar", 2013, 2000.00)

# Test the get_age method
print(f"Gibson L-5 CES get_age() - Expected 100. Got {gibson_guitar.get_age()}")
print(f"Another Guitar get_age() - Expected 9. Got {another_guitar.get_age()}")

# Test the is_vintage method
print(f"Gibson L-5 CES is_vintage() - Expected True. Got {gibson_guitar.is_vintage()}")
print(f"Another Guitar is_vintage() - Expected False. Got {another_guitar.is_vintage()}")

# Example of a guitar that is exactly 50 years old
fifty_year_old_guitar = Guitar("50-year old guitar", 1972, 3000.00)
print(f"50-year old guitar is_vintage() - Expected True. Got {fifty_year_old_guitar.is_vintage()}")

# Example of a mistake in the is_vintage method implementation
# Assuming the method was incorrectly implemented to always return False
incorrect_guitar = Guitar("Incorrect Guitar", 1972, 4000.00)
incorrect_guitar.is_vintage = lambda: False  # Incorrect implementation
print(f"Incorrect guitar is_vintage() - Expected True. Got {incorrect_guitar.is_vintage()}")
