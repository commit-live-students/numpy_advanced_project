# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(team):
    # Your Solution
    data = ipl_matches_array
    match = list()
    toss_win = 0
    for i in range(data.shape[0]):
        match.append(data[i][0])
    match = list(set(match))
    match.sort()
    print(match)
    #print(data[0][5])
    for m in match:
        for row in data:
            if row[0]== m and row[5]==team and row[11] == b'0.1':
                print(row[0],row[5],row[11])
                toss_win+=1
    return int(toss_win/2)

get_toss_win_count(b'Mumbai Indians')



