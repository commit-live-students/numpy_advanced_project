# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_all_sixes_filter():
    a=[]
    run_6=ipl_matches_array[:,16].astype(np.int16)==6
    return run_6
    
    
    


get_all_sixes_filter()


