# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_all_sixes_filter():
    a=ipl_matches_array
    b=np.array(a[:,16].astype('int16')==6)
    return b
c=get_all_sixes_filter()
c


