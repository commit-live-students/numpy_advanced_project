# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_all_sixes_filter ():
    var = np.array(ipl_matches_array[:,[16]])
    return np.array([myfunc(row,6) for row in var])

def myfunc(row,number):
    print(row[0])
    return row[0].astype(int) == number



