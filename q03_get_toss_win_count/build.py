import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def get_toss_win_count(team):
    a=ipl_matches_array[:,5]
    itemindex=np.where(a==team)
    ilst = list(itemindex)
    reqd_rows=ipl_matches_array[ilst]
    c= reqd_rows[:,[0,5]]
    d=np.unique(c)
    return (len(d)-1)
