import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir),'..'))

from unittest import TestCase
from q01_get_total_deliveries_players.build import get_total_deliveries_played

class TestGet_total_deliveries_played(TestCase):
    def test_get_total_deliveries_played(self):

        tendulkar_total = get_total_deliveries_played('SR Tendulkar')
        self.assertTrue(tendulkar_total == 84)
