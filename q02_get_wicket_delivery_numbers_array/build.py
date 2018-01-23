#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
#11 20
#Your Solution
def get_wicket_delivery_numbers_array(player):
    wicket_delivery = ipl_matches_array[:,[11,20]]
    ans = wicket_delivery[wicket_delivery[:,1]==player]
    ans1 = ans[:,0]
    return ans1
