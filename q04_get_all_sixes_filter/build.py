
# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_all_sixes_filter():
    runs=ipl_matches_array[:,16].astype(np.int16)
    sixers = (runs == 6)
    return sixers

print(get_all_sixes_filter())




#Your Solution




