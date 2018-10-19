# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_wicket_delivery_numbers_array(player):
    data = ipl_matches_array
    ball = []
    for row in data:
        if(row[20] == player):
            print(row[11])
            ball.append(row[11])
    nparr = np.array(ball)
    #print(nparr.shape)
    return nparr


#get_wicket_delivery_numbers_array(b'ST Jayasuriya')
    
#Your Solution




