
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_toss_win_count(team):
    np.set_printoptions(threshold=np.nan)
    total_num_tosses_won = len (set (ipl_matches_array[:,6]))
    return total_num_tosses_won
get_toss_win_count(b'Mumbai Indians')


