# Default imports
import numpy as np
import pandas as pd
batsman = raw_input('Enter batsman: ')
def get_wicket_delivery_numbers_array(batsman):
    ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=0, delimiter=",")
    delivery_no = ipl_matches_array[:,11]
    player_out = ipl_matches_array[:,20]
    s = pd.Series(data = delivery_no, index = player_out )
    print s[batsman].values
     #s[player].values()

get_wicket_delivery_numbers_array(batsman)
