#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

# Check the "runs" column if its 6 then append value as 'True' else 'False'
def get_all_sixes_filter():
    var=[]
    for element in ipl_matches_array:
        if int(element[16])== 6:
            var.append(True)
        else:
            var.append(False)
    variable =np.array(var)
    return variable
#Another way out
#ipl_matches_array[:, 16].astype(np.int16) == 6
