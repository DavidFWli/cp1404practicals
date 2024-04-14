from prac_06.car import Car
from taxi import Taxi

# Create a new taxi object
my_taxi = Taxi("Prius 1", 100)

# Drive the taxi 40 km
my_taxi.drive(40)

# Print the taxi's details and the current fare
print(my_taxi)

# Restart the meter and drive the car 100 km
my_taxi.start_fare()
my_taxi.drive(100)

# Print the details and the current fare
print(my_taxi)