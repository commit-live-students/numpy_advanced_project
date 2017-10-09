# %load q03_get_toss_win_count/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
#Your Solution
def get_toss_win_count(team="Mumbai Indians"):
    count=0
    tossfil=(ipl_matches_array[:,5]==team)
    tossteamlist=ipl_matches_array[tossfil,0:6]
    #print(tossteamlist)
    unique=np.unique(tossteamlist[:,0])
    #print(unique)
    count=len(unique)
    return count
#t=get_toss_win_count()
#print(t)
