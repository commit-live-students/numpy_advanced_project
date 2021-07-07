# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_toss_win_count(toss):
    # count=0
    #row=0 column=5
    toss_winner = ipl_matches_array[:,(0,5)]
    #if toss_winner is team then add it into tosswinnercode 
    index = np.where(toss_winner[:,1]==toss)
    tosswinnerscode = toss_winner[index][:,0]
    #counting all the matchwinner in single list
    return  len(np.unique(tosswinnerscode)) 
    #input as mumbai indian
print(get_toss_win_count(b'Mumbai Indians'))


    






