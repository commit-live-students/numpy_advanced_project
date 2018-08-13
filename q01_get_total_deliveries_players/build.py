import numpy as np

ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_total_deliveries_played(batsman1):
    a=ipl_matches_array[:,13]
    b= a[a==batsman1]
    return b.size  
