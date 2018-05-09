# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    team_records = ipl_matches_array[:, 16]
    
    team_filter = (team_records ==b'6')
    print(team_filter)
    return team_filter
get_all_sixes_filter()
                                     
                                     

