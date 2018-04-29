# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    matchCode=[]
    count=0
    for data in ipl_matches_array:
        if data[0] not in matchCode:
            matchCode.append(data[0])
            #print(data[5])
            if team in str(data[5]):
                count=count+1
    return(count)
    


