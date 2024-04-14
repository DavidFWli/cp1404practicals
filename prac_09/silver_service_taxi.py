from taxi import Taxi

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness, price_per_km):
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        return super().get_fare() + SilverServiceTaxi.flagfall

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km plus flagfall of ${SilverServiceTaxi.flagfall:.2f}"
