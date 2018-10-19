# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    #Returning boolean index array where element value for runs is 6.
    return ipl_matches_array[:,-7]==b'6'

#Call to the function
get_all_sixes_filter()



