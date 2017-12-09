# Default imports
import numpy as np

def get_total_deliveries_played (batsman):
    ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
    allbatsman = ipl_matches_array[0:len(ipl_matches_array),13]
    unique, counts = np.unique(allbatsman, return_counts=True)
    all_delv = dict(zip(unique, counts))
    delv_played = all_delv.get(batsman,None)
    return delv_played
