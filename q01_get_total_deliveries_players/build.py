# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

# Your Solution
def get_total_deliveries_played(batsman):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
    a=ipl_matches_array
    p=[]
    q=[]
    for i in range(len(a)):
        b=tuple((a[i][13],a[i][11]))
        p.append(b)
    for i in (p):
            if i[0]==batsman:
                q.append(float(i[1]))
    return len(q)
    
c=get_total_deliveries_played(b'SR Tendulkar')

c




