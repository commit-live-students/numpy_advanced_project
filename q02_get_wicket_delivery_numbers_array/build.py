#Default Imports
import numpy as np
from numpy import array
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    cnt=[]
    for matches in ipl_matches_array:
        if matches[20]== batsman:
            cnt.append(matches[11])
    deliveries=array(cnt)
    return deliveries

get_wicket_delivery_numbers_array('ST Jayasuriya')
