# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np
from numpy import array
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def get_wicket_delivery_numbers_array(batsman):
    cnt=[]
    for matches in ipl_matches_array:
        if matches[-3] == batsman:
            cnt.append(matches[11])
    cnt1=array(cnt)
    return cnt1

res=get_wicket_delivery_numbers_array('ST Jayasuriya')
print res
