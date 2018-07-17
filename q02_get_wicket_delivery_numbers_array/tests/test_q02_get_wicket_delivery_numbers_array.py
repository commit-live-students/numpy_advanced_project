import numpy as np
from unittest import TestCase
from ..build import get_wicket_delivery_numbers_array

class TestGet_wicket_delivery_numbers_array(TestCase):
    def test_get_wicket_delivery_numbers_array(self):
        deliveries = get_wicket_delivery_numbers_array(b'ST Jayasuriya')
        self.assertTrue(np.all(deliveries == np.array([b'3.2', b'14.4',b'1.4'])), 'Expected Value does not match with the given values' )
