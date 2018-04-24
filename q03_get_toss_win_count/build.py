# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(teamName):
    matchId , index = np.unique(ipl_matches_array[:,0].astype(str),return_index=True)
    tossWinnerTeams = ipl_matches_array[index,5].astype(str)
    matchCount,matchIndex = np.unique(tossWinnerTeams,return_counts = True)
    matchDict = dict(zip(matchCount, matchIndex))
    print(matchDict[teamName])
    return matchDict[teamName]
    
get_toss_win_count('Mumbai Indians')

