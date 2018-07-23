# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
        toss_winners =  ipl_matches_array[:,(0,5)]
        filtered_index= np.where  (toss_winners[:,1]==team)
        matchcodes_where_toss_won= toss_winners[filtered_index][:,0]
        return  len(np.unique(matchcodes_where_toss_won)) 
    
print(get_toss_win_count(b'Mumbai Indians'))



