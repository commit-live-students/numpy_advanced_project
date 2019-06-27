# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')



#funtion statement
def get_all_sixes_filter():
    ''' filter to get only the records with only 6 '''
    Records = ipl_matches_array[:,16].astype('int32')==6
    return Records

#Call the funtion
(get_all_sixes_filter())



