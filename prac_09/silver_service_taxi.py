from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50  # Class variable for the flagfall charge

    def __init__(self, model, fuel_capacity, fanciness):
        super().__init__(model, fuel_capacity)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness  # Customize the price_per_km based on fanciness

    def get_fare(self):
        fare = super().get_fare() * self.price_per_km  # Call the parent's get_fare() method and multiply by fanciness
        fare += SilverServiceTaxi.flagfall  # Add the flagfall charge
        return fare

    def __str__(self):
        base_str = super().__str__()  # Reuse the parent's __str__ method
        return f"{base_str}, {self.price_per_km:.2f}/km plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"