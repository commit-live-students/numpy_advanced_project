import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))

from unittest import TestCase
from q06_create_runs_series.build import create_runs_series
import numpy as np

class TestCreate_runs_series(TestCase):
    def test_create_runs_series(self):
        match_code = '392203'

        # Mumbai Indians
        expected = None
        # ... same code as above func
        actual = create_runs_series(match_code)
        self.assertFalse(np.all(expected == actual))
