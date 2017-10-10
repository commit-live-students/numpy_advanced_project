# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
import pandas as pd
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
#11,20
def get_wicket_delivery_numbers_array(player):
    fil1=ipl_matches_array[:,20]==player
    x=ipl_matches_array[fil1,11]
    return x
#get_wicket_delivery_numbers_array('ST Jayasuriya')
#y=pd.Series(ipl_matches_array[:,20])
#pd.Series(ipl_matches_array[:,11],ipl_matches_array[:,20])
