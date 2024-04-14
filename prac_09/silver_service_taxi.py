class Taxi:
    def __init__(self, fuel, odometer, price_per_km=2.46):  # 假设基础价格是2.46$/km
        self.fuel = fuel
        self.odometer = odometer
        self.price_per_km = price_per_km  # 设置基础价格每公里

    def __str__(self):
        return f"{self.__class__.__name__}, fuel={self.fuel}, odo={self.odometer}, current_fare={self.current_fare}km on current fare"

    def calculate_fare(self, distance):
        self.current_fare += distance * self.price_per_km


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, fuel, odometer, fanciness):
        super().__init__(fuel, odometer)  # 调用父类的__init__方法
        self.fanciness = fanciness
        self.price_per_km = self.price_per_km * self.fanciness  # 调整价格每公里

    def __str__(self):
        return f"{super().__str__()}, {self.price_per_km}$/km plus flagfall of ${self.flagfall}"

    def calculate_fare(self, distance):
        self.current_fare = self.flagfall
        super().calculate_fare(distance)
