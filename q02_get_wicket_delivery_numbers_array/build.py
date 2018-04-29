import pandas as pd
import numpy as np

def get_wicket_delivery_numbers_array(batsman):
    ipl_data=pd.read_csv('./data/ipl_matches_small.csv')
    out_deliveries=ipl_data[ipl_data['player_out']==batsman]['delivery']
    return np.array(out_deliveries)
ipl_data=get_wicket_delivery_numbers_array('ST Jayasuriya')
ipl_data

