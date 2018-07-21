# %load q01_get_total_deliveries_players/build.py
# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


# Function to calculate number of deliveries played
def get_total_deliveries_played(batsman):
    delivery = 0
    for i in list((ipl_matches_array[:,-10])):
        if i == batsman:
            delivery+=1
    return delivery

#Function call
get_total_deliveries_played(b'SR Tendulkar')
#print(get_total_deliveries_played('SR Tendulkar'))


