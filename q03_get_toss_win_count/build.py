# %load q03_get_toss_win_count/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution
def get_toss_win_count(team="Mumbai Indians"):
    test=ipl_matches_array[1:,[0,5]]
    #print(test)
    t1=test[test[:,1]=="Mumbai Indians"]
    t2=np.unique(t1[:,0])
    return(len(t2))
get_toss_win_count()
