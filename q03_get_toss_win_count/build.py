# %load q03_get_toss_win_count/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

#Your Solution
def get_toss_win_count(team="Mumbai Indians"):
    count=0
    tossfil=(ipl_matches_array[:,5]==team)
    tossteamlist=ipl_matches_array[tossfil,5]
    #print(tossteamlist)
    count=len(tossteamlist)
    return count
#t=get_toss_win_count()
#print(t)
