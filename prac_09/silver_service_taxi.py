from taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness, price_per_km):
        super().__init__(name, fuel)
        self.price_per_km *= fanciness
        self.flagfall = SilverServiceTaxi.flagfall  # 设置self.flagfall为类属性flagfall的值

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare_distance}km on current fare, ${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}"
