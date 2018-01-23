#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

#Your Solution
def create_runs_series(match_code):
    pstart = ipl_matches_array[:,[0,11,16]]
    pseries = pstart[pstart[:,0]==match_code]
    pseries1 = pseries[:,[1,2]]
    ans = pd.Series(pseries1[:,1],index=pseries1[:,0])
    return ans
