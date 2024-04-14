from taxi import Taxi  # Assuming Taxi is the base class defined in taxi.py


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, model, price_per_km, fanciness_factor):
        self.model = model
        self.price_per_km = price_per_km
        self.fanciness_factor = fanciness_factor

    def get_fare(self, distance):
        base_fare = self.price_per_km * distance
        enhanced_fare = base_fare * self.fanciness_factor
        rounded_fare = round(enhanced_fare + self.flagfall, 1)
        return rounded_fare

    def __str__(self):
        base_str = super().__str__()
        return f"{base_str}, {self.price_per_km:.2f}/km plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"
