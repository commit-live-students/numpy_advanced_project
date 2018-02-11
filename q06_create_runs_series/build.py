# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def create_runs_series(match_code):
    deli_with_runs = ipl_matches_array[:,[0,11,16]]
    match_codes = deli_with_runs[deli_with_runs[:,0] == match_code]
    semi_final_answer = match_codes[:,[1,2]]
    final_answer = pd.Series(semi_final_answer[:,1], index=semi_final_answer[:,0])
    return final_answer


