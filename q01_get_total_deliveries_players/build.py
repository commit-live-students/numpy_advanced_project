# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np
import pandas as pd

ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution

def get_total_deliveries_played(batsman):
    #Approach 1 - Using numpy
    df = pd.read_csv('data/ipl_matches_small.csv')
    header_list = list(df)
    batsman_list = ipl_matches_array[:,header_list.index('batsman')]
    return np.count_nonzero(batsman_list == batsman)

    #Approach 2 - Converting numpy array to list
    batsman_list_2nd = ipl_matches_array[:,header_list.index('batsman')].tolist()
    print(batsman_list_2nd.count(batsman))
    
    #Approach 3 - Conventional
    deliveries = 0
    batsman_list_3rd = ipl_matches_array[:,header_list.index('batsman')].tolist()
    for batsman_name in batsman_list_3rd:
        if (batsman_name == batsman):
            deliveries = deliveries + 1
    print(deliveries)

get_total_deliveries_played(b'SR Tendulkar')

