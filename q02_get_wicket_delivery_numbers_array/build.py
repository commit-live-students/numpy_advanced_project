# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(name):
    player_out_ball=[]
    total_deliveries=0
    for i in range(0,len(ipl_matches_array),1):
        if str(ipl_matches_array[i,20], 'utf-8')==name:
            temp=str(ipl_matches_array[i,11], 'utf-8')
            player_out_ball.append(float(temp))
            
    return player_out_ball


