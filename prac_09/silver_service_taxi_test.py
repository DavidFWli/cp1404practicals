from silver_service_taxi import SilverServiceTaxi


def silver_service_taxi_test():
    taxi = SilverServiceTaxi("Hummer", 1.23, 2)
    distance = 18
    expected_fare = taxi.get_fare(distance)
    actual_fare = taxi.get_fare(distance)
    assert actual_fare == expected_fare, f"Fare calculation is incorrect. Expected: ${expected_fare}, Actual: ${actual_fare}"
    print(f"The taxi fare is ${actual_fare}")


silver_service_taxi_test()
