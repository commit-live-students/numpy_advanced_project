# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution

def get_all_sixes_filter():
    runArray = ipl_matches_array[:,16].astype(int)
    #unique , count = np.unique(runArray,return_counts = True ) 
    #dictRuns = dict(zip(unique,count))
    boolArray = runArray == 6
    print(boolArray)
    return boolArray
get_all_sixes_filter()

