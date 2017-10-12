# Default imports
import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(batsmen):
    batsmen1 = batsmen
    #ipl_matches_array = np.genfromtxt(path,dtype='|S50', skip_header=1,delimiter = ',')
    del_batsman_array = ipl_matches_array[:,(11,13)]
    count = 0
    for i in del_batsman_array:
        if i[1] == batsmen1:
            count = count + 1

    return count
get_total_deliveries_played('SR Tendulkar')
