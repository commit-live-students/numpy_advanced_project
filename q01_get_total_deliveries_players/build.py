# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman_name): 
    print(batsman_name)
    batsman=ipl_matches_array[:,13]
    unique, counts = np.unique(batsman, return_counts=True)
    batsman_dict=(dict(zip(unique, counts)))
    print (type(batsman_dict))
    print(batsman_dict[batsman_name])
    return(batsman_dict[batsman_name])

get_total_deliveries_played(b'SR Tendulkar')


