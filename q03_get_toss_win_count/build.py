# %load q03_get_toss_win_count/build.py
#Default Imports
#from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
path = "./data/ipl_matches_small.csv"
def get_toss_win_count(team="Mumbai Indians"):
    ipl_matches_array = np.genfromtxt(path,dtype='|S50',skip_header=1,delimiter=',')
#Your Solution
    a=ipl_matches_array[0:,5] == team
    return int(len(np.unique(ipl_matches_array[a][0:1451,0])))
