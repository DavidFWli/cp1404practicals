"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car

# Create a new Car object called "limo" that is initialised with 100 units of fuel.
limo = Car(100)

# Add 20 more units of fuel to this new car object using the add_fuel method.
limo.add_fuel(20)

# Print the amount of fuel in the car.
print(f"Limo has fuel: {limo.fuel}")

# Attempt to drive the car 115 km using the drive method.
driven_distance = limo.drive(115)

# Print the distance actually driven.
print(f"Limo driven distance: {driven_distance} km")

# Now add the __str__ method to the Car class in car.py.
# This method will be responsible for printing the Car object in a human-readable format.