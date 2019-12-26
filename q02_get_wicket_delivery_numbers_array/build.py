# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array (name):
    var = np.array(ipl_matches_array[:,[11,-3]])
    return np.asarray(var[[myfunc(row,name) for row in var]][:,[0]].reshape(1,3))

def myfunc(row,name):
    return row[1] == name


