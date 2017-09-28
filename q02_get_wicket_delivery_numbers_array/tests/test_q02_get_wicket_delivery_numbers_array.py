import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),'..'))

import numpy as np
from unittest import TestCase
from q02_get_wicket_delivery_numbers_array.build import get_wicket_delivery_numbers_array

class TestGet_wicket_delivery_numbers_array(TestCase):
    def test_get_wicket_delivery_numbers_array(self):
        deliveries = get_wicket_delivery_numbers_array('ST Jayasuriya')
        self.assertTrue(np.all(deliveries == np.array(['3.2', '14.4', '1.4'])))