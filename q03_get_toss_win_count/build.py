# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution

def get_toss_win_count(team):
    
    
    #team = team.encode() #to convert string into byte

    #list of unique matches
    unique_matches = np.unique(ipl_matches_array[:, [0,3,4,5]],axis = 0)
   
    
    #comparing team name with unique matches then select column which has data of team who win toss
    #count = len(unique_matches[unique_matches[:,3] == team][:,3])
    
    return len(unique_matches[unique_matches[:,3] == team][:,3])


team_name = b'Mumbai Indians'
get_toss_win_count(team_name)



