# Default imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
from pandas import Series, DataFrame
import pandas as pd
import numpy as np

def get_total_deliveries_played(batsman_name):
    all_batsman = ipl_matches_array[:,13:14]
    df = DataFrame(all_batsman)
    df.columns= ['Name']
    #print df.Name.unique()
    #input_name = str(raw_input('Enter name of batsman from the list above'))
    balls_faced = df.Name.value_counts()[batsman_name]

    return balls_faced

print get_total_deliveries_played(batsman_name='SR Tendulkar')
