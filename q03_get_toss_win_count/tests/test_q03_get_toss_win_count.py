import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..'))

from unittest import TestCase
from q03_get_toss_win_count.build import get_toss_win_count

class TestGet_toss_win_count(TestCase):
    def test_get_toss_win_count(self):
        count = get_toss_win_count('Mumbai Indians')
        self.assertTrue(count == 2)
