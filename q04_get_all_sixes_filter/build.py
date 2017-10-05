#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
def get_all_sixes_filter():
    records_six = ipl_matches_array[ipl_matches_array[:, 16].astype(np.int16) == 6][:,[0,16]]

    a = np.vstack({tuple(row) for row in records_six})
    return records_six[:,0]
print(get_all_sixes_filter())
