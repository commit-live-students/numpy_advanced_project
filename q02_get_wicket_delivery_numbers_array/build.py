#Default Imports
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
#from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
ipl_matches_array = np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", delimiter=",")
#Your Solution
def get_wicket_delivery_numbers_array():
    players = DataFrame(ipl_matches_array[:, :])



    print players
print get_wicket_delivery_numbers_array()
