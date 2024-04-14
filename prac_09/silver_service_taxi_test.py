from silver_service_taxi import SilverServiceTaxi


def test_silver_service_taxi():
    taxi = SilverServiceTaxi(fuel=200, odometer=0, fanciness=2)
    assert taxi.price_per_km == 4.92  # Assuming the base price_per_km for Taxi is 2.46
    taxi.calculate_fare(18)
    assert taxi.current_fare == 48.78  # Flagfall of 4.50 + 18km * 2.46$/km * 2 (fanciness)

    print(taxi)
    # Output should be: SilverServiceTaxi, fuel=200, odo=0, 0km on current fare, 4.92$/km plus flagfall of $4.50


if __name__ == "__main__":
    test_silver_service_taxi()
