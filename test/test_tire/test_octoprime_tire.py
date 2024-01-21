import unittest

from cars.tire import OctoprimeTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensors = [0.9, 0.9, 0.9, 0.5]
        tire = OctoprimeTire(sensors)
        self.assertTrue(tire.needs_service())
        
    def test_needs_service_false(self):
        sensors = [0.5, 0.4, 0.1, 0.9]
        tire = OctoprimeTire(sensors)
        self.assertTrue(tire.needs_service())
        