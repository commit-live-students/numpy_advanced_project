#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
import pandas as pd
#Your Solution
def get_all_sixes_filter():
    rows = (ipl_matches_array[:,[16]]).flatten()
    return rows == '6'
