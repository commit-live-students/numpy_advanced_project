#%load q04_get_all_sixes_filter/build.py


import numpy as np


path='./data/ipl_matches_small.csv'

def get_all_sixes_filter():
    

    ipl_matches_array=np.genfromtxt(path,delimiter=',',dtype='|S50',skip_header=1)
    #arr_6=(arr[:,16]==b'6')
    
    return ipl_matches_array[:,16].astype(np.int16)==6


get_all_sixes_filter()
    
    



