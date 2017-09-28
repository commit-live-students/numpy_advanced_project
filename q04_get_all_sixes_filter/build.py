#Default Imports
import sys, os
sys.path.append(os.path.join(os.path.dirname(os.curdir), '..','..'))

from q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
def get_all_sixes_filter():
    return (ipl_matches_array[:, 16].astype(np.int16) == 6)