import unittest
from unreliable_car import UnreliableCar


class TestUnreliableCar(unittest.TestCase):
    def test_drive_reliability(self):
        # Test driving with high reliability
        car1 = UnreliableCar("Car1", 50, 90)
        self.assertEqual(car1.drive(30), 30)  # Should drive successfully

        # Test driving with low reliability
        car2 = UnreliableCar("Car2", 50, 10)
        self.assertEqual(car2.drive(30), 0)  # Should not drive due to low reliability

    def test_drive_fuel(self):
        # Test driving with fuel constraint
        car = UnreliableCar("Car", 20, 100)
        self.assertEqual(car.drive(30), 20)  # Should drive only 20 km due to fuel constraint


if __name__ == "__main__":
    unittest.main()
