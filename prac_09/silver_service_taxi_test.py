from silver_service_taxi import Taxi, SilverServiceTaxi


def test_silver_service_taxi():
    # Test SilverServiceTaxi class
    # Store the adjusted price per kilometer based on fanciness
    adjusted_price_per_km = Taxi.price_per_km * 2

    taxi = SilverServiceTaxi(fuel=200, odometer=0, fanciness=2)

    # Assert that the price per kilometer is correctly adjusted
    assert taxi.price_per_km == adjusted_price_per_km

    # Calculate the fare for a distance of 18km
    print("Calculating fare for 18km...")
    taxi.calculate_fare(18)

    # Assert that the current fare is correctly calculated
    expected_fare = (adjusted_price_per_km * 18) + SilverServiceTaxi.flagfall
    assert taxi.current_fare == expected_fare

    # Get the expected string representation based on the current state of the taxi
    expected_str = (
        f"SilverServiceTaxi, fuel={taxi.fuel}, odo={taxi.odometer}, "
        f"{taxi.odometer}km on current fare, ${taxi.price_per_km:.2f}/km plus flagfall of $4.50"
    )

    # Assert that the string representation is as expected
    print(f"Actual taxi string representation:")
    print(str(taxi))
    assert str(taxi) == expected_str

    print(taxi)
    print("All tests passed!")


if __name__ == "__main__":
    test_silver_service_taxi()
