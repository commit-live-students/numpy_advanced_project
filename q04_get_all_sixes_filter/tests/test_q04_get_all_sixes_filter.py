import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))
from q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

from unittest import TestCase
from q04_get_all_sixes_filter.build import get_all_sixes_filter

class TestGet_all_sixes_filter(TestCase):
    def test_get_all_sixes_filter(self):
        expected_filter = (ipl_matches_array[:, 16].astype(np.int16) == 6)
        actual_filter = get_all_sixes_filter()
        self.assertTrue(np.all(expected_filter == actual_filter))

