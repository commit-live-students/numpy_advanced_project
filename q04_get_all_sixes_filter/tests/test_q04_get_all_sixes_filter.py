import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))

import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

from unittest import TestCase
from q04_get_all_sixes_filter.build import get_all_sixes_filter

class TestGet_all_sixes_filter(TestCase):
    def test_get_all_sixes_filter(self):
        expected_filter = (ipl_matches_array[:, 16].astype(np.int16) == 6)
        actual_filter = get_all_sixes_filter()
        self.assertTrue(np.all(expected_filter == actual_filter),'Expected Value does not match with the given values')
