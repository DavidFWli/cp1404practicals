class Taxi:
    def __init__(self, name, fuel, odometer, current_fare_km, rate):
        self.name = name
        self.fuel = fuel
        self.odometer = odometer
        self.current_fare_km = current_fare_km
        self.rate = rate

    def drive(self, distance):
        if self.fuel == 0:
            print("Insufficient fuel. Refueling required.")
            return None

        actual_distance = min(distance, self.fuel)
        self.fuel -= actual_distance
        self.odometer += actual_distance
        self.current_fare_km += actual_distance
        cost = actual_distance * self.rate
        if self.name == "Limo":
            cost += 4.50  # flagfall

        return cost

    def __str__(self):
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}, " \
               f"current_fare_km={self.current_fare_km}, rate=${self.rate}/km"

def print_bill_to_date(total_bill):
    print(f"Bill to date: ${total_bill:.2f}")

def main():
    taxis = [
        Taxi("Prius", 100, 0, 0, 1.23),
        Taxi("Limo", 100, 0, 0, 2.46),
        Taxi("Hummer", 200, 0, 0, 4.92)
    ]
    chosen_taxi = None  # 初始化chosen_taxi为None
    total_bill = 0.0

    while True:
        print("q)uit, c)hoose taxi, d)rive")
        choice = input(">>> ").lower()  # 将输入转换为小写
        if choice == "q":
            print(f"Total trip cost: ${total_bill:.2f}")
            print("Taxis are now:")
            for taxi in taxis:
                print(taxi)
            break
        elif choice == "c":
            print("Taxis available:")
            for index, taxi in enumerate(taxis):
                print(f"{index} - {taxi}")
            choice = input("Choose taxi: ")
            try:
                chosen_taxi = taxis[int(choice)]  # 赋值给chosen_taxi
                print("Bill to date: ${:.2f}".format(total_bill))
            except (IndexError, ValueError):
                print("Invalid taxi choice")
                print("Bill to date: ${:.2f}".format(total_bill))
                chosen_taxi = None  # 如果选择无效，重置chosen_taxi为None
        elif choice == "d":
            if not chosen_taxi:
                print("You need to choose a taxi before you can drive")
                print("Bill to date: ${:.2f}".format(total_bill))
                continue  # 使用continue跳过当前循环迭代
            distance = input("Drive how far? ")
            try:
                distance = float(distance)
                cost = chosen_taxi.drive(distance)
                if isinstance(cost, str):
                    print(cost)
                else:
                    total_bill += cost
                    print(f"Your {chosen_taxi.name} trip cost you ${cost:.2f}")
                    print(f"Bill to date: ${total_bill:.2f}")
            except ValueError:
                print("Invalid distance. Please enter a number.")
                print(f"Bill to date: ${total_bill:.2f}")
        else:
            print("Invalid option")
            print("Bill to date: ${:.2f}".format(total_bill))



if __name__ == "__main__":
    main()
