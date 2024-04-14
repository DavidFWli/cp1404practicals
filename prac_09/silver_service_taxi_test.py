from silver_service_taxi import SilverServiceTaxi


# Test the calculation of fares for SilverServiceTaxi
def test_silver_service_fare():
    hummer = SilverServiceTaxi("Hummer", 200, 4, 4.92)
    hummer.start_fare()
    hummer.drive(18)
    assert hummer.get_fare() == 48.78


test_silver_service_fare()
