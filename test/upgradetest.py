import unittest
from datetime import datetime, timedelta
from car import CarFactory

class TestBattery(unittest.TestCase):
    def test_spindler_battery_service(self):
        # Create a Spindler battery with a last service date three years ago
        last_service_date = datetime.now() - timedelta(days=3*365)
        battery = CarFactory.create_spindler_battery(last_service_date)

        # Check if the battery needs service
        self.assertTrue(battery.needs_service())

    def test_carrigan_tire_service(self):
        # Create Carrigan tires with tire wear array indicating high wear on one tire
        tire_wear = [0.8, 0.2, 0.3, 0.4]
        needs_service = CarFactory.check_tire_service('Carrigan', tire_wear)

        # Check if the tires need service
        self.assertTrue(needs_service)

    def test_octoprime_tire_service(self):
        # Create Octoprime tires with tire wear array indicating high wear on all tires
        tire_wear = [0.9, 0.9, 0.9, 0.9]
        needs_service = CarFactory.check_tire_service('Octoprime', tire_wear)

        # Check if the tires need service
        self.assertTrue(needs_service)

if __name__ == '__main__':
    unittest.main()
