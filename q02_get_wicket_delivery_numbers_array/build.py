# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

#from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=0, delimiter=",")
#Your Solution
from pprint import pprint
#pprint(ipl_matches_array)
def get_wicket_delivery_numbers_array(player):
    #pprint(ipl_matches_array[50:,20])
    fil1=(ipl_matches_array[:,13]==player)

    #rows_with_correct_player=ipl_matches_array[fil1,11]
    fil2=(ipl_matches_array[:,20]==player)
    fil3=fil1&fil2
    #rows_with_correct_player=ipl_matches_array[fil1,:]
    out_rows=ipl_matches_array[fil3,11]
    #print(rows_with_correct_player)
    return (out_rows)



#type(get_wicket_delivery_numbers_array("SR Tendulkar"))
#sr=get_wicket_delivery_numbers_array("SR Tendulkar")
#print(sr)
#print(type(sr))
