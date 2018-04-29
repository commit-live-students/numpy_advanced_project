# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

def get_all_sixes_filter():
    #array=np.array(6==data[-7].astype(np.int16))
    for data in ipl_matches_array:
        array=np.array(data[-7])
        return(array.astype(np.int16)==6)
     

