# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_toss_win_count(team):
    a=ipl_matches_array
    count=0
    q=[]
    for i in range(len(a)):
        b=tuple((a[i][0],a[i][5]))
        q.append(b)
    q=set(q)
    for i in q:
        if i[1]==team:
            count=count+1
    return count
        
        
c= get_toss_win_count(b'Mumbai Indians')
c


