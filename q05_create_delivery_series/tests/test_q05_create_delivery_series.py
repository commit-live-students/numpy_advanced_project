import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
import pandas as pd
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
from q05_create_delivery_series.build import create_delivery_series



from unittest import TestCase


class TestCreate_delivery_series(TestCase):
    def test_create_delivery_series(self):
        expected = pd.Series(ipl_matches_array[:, 11])
        actual = create_delivery_series()
        self.assertTrue(np.all(expected == actual),'Expected Value does not match with the given values')
