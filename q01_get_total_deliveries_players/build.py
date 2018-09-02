# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_total_deliveries_played(batsman):
    # Your Solution
    data = ipl_matches_array
    ball = []
    for row in data:
        if(row[13] == batsman):
            #print(type(row[11]))
            ball.append(row[11])
    #print(len(ball))
    return len(ball)


#get_total_deliveries_played(b'SR Tendulkar')

          


