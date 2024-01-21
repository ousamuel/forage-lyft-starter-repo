import unittest

from cars.tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        sensors = [0.5, 0.9, 0.8, 0.1]
        tire = CarriganTire(sensors)
        self.assertTrue(tire.needs_service())
        
    def test_needs_service_false(self):
        sensors = [0.5, 0.7, 0.7, 0.1]
        tire = CarriganTire(sensors)
        self.assertTrue(tire.needs_service())
        