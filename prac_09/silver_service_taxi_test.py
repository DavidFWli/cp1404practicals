from silver_service_taxi import SilverServiceTaxi

def test_silver_service_taxi():
    taxi = SilverServiceTaxi("Hummer", 200, 2)
    taxi.drive(18)
    expected_fare = 48.78  # Calculated fare for a 18 km trip in a SilverServiceTaxi with fanciness of 2
    assert taxi.get_fare() == expected_fare, "Fare calculation is incorrect"
    print(taxi)  # Output the taxi information for verification

if __name__ == "__main__":
    test_silver_service_taxi()