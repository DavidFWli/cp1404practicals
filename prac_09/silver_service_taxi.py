class Taxi:
    price_per_km = 2.46  # 类属性，定义每公里的价格

    def __init__(self, fuel, odometer):
        self.fuel = fuel
        self.odometer = odometer
        self.current_fare = 0

    def calculate_fare(self, distance):
        self.current_fare = self.price_per_km * distance

    def __str__(self):
        return f"{self.__class__.__name__}, fuel={self.fuel}, odo={self.odometer}, {self.current_fare}km on current fare, ${self.price_per_km:.2f}/km"


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, fuel, odometer, fanciness):
        super().__init__(fuel, odometer)  # 调用父类的构造函数
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness  # 设置每公里的价格，基于豪华程度

    def calculate_fare(self, distance):
        super().calculate_fare(distance)  # 调用父类的计算费用方法
        self.current_fare += self.flagfall  # 添加起步价到总费用

    def __str__(self):
        return (
            f"SilverServiceTaxi, fuel={self.fuel}, odo={self.odometer}, "
            f"{self.odometer}km on current fare, ${self.price_per_km:.2f}/km plus flagfall of $4.50"
        )
