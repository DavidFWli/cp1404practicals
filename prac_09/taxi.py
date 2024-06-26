from car import Car


class Taxi(Car):
    """Specialised version of a Car that includes fare costs."""
    price_per_km = 1.23  # Class variable

    def __init__(self, name, fuel):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.current_fare_distance = 0

    def __str__(self):
        """Return a string representation of the Taxi."""
        car_details = super().__str__()  # Get the parent class details
        fare_details = f"{self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km"
        return f"{car_details}, {fare_details}"

    def get_fare(self):
        """Return the total price for the taxi trip including the flagfall, rounded to the nearest 10 cents."""
        fare = self.price_per_km * self.current_fare_distance + self.flagfall
        rounded_fare = round(fare, -1)  # Round to the nearest 10 cents
        return rounded_fare

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven
