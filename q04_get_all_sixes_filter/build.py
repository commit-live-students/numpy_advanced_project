from pandas import Series, DataFrame
import pandas as pd
import numpy as np
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Default Imports


#Your Solution
#Your Solution
def get_all_sixes_filter():
    runs = (ipl_matches_array[:, 16].astype(np.int16) == 6)
    return (runs)
print get_all_sixes_filter()
