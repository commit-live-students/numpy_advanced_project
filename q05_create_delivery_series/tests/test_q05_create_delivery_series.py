import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))

from q01_get_total_deliveries_players.build import ipl_matches_array
from q05_create_delivery_series.build import create_delivery_series

import pandas as pd
import numpy as np


from unittest import TestCase


class TestCreate_delivery_series(TestCase):
    def test_create_delivery_series(self):
        expected = pd.Series(ipl_matches_array[:, 11])
        actual = create_delivery_series()
        self.assertTrue(np.all(expected == actual))
