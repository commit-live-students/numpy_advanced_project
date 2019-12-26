import pandas as pd
import numpy as np
def get_wicket_delivery_numbers_array(batsman):
    ipl_matches_array = pd.read_csv('data/ipl_matches_small.csv')
    delivery = ipl_matches_array['delivery']
    bool_data_time = ipl_matches_array['player_out'] == batsman
    nparr = delivery[bool_data_time].astype(np.str)
    
    return nparr
get_wicket_delivery_numbers_array('ST Jayasuriya')




