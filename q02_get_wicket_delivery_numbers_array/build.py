#Default Imports
import numpy as np

#from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
ipl_matches_array =np.genfromtxt("/home/darshind/Workspace/code/numpy_advanced_project/data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    data = ipl_matches_array[ipl_matches_array[:,20] == batsman]
    return data[:,11]
print get_wicket_delivery_numbers_array(batsman = 'AC Gilchrist')
