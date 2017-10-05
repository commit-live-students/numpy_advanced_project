# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

# Your Solution

def get_wicket_delivery_numbers_array(player):
    #print(player)
    batsman = ipl_matches_array[ipl_matches_array[:,13]==player]
    #print(batsman)
    #outballs = np.where(batsman[:-3]==player)
    #count = 0
    balls = batsman[:,11][batsman[:,-3]==player]

    #if batsman[:-3]=='ST Jayasuriya':
    return balls
