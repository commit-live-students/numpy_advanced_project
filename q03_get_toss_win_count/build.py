# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    match_codes = []
    counter = 0
    rows = ipl_matches_array.shape[0]
    for i in range(0,rows):
        if ipl_matches_array[i][3] == team or ipl_matches_array[i][4] == team:
            
            match_code = ipl_matches_array[i][0]
            if match_code not in match_codes:
                #print(ipl_matches_array[i][4])
                match_codes.append(match_code)
                if ipl_matches_array[i][5] == team:
                    counter = counter + 1
    return counter
get_toss_win_count(b'Mumbai Indians')



