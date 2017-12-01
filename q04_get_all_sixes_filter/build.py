#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np

#Your Solution
def get_all_sixes_filter():
    six=[]
    for item in ipl_matches_array[:,16:17]=='6':
        six.append(item[0])
    return six
