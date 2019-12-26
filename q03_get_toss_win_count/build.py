# %load q03_get_toss_win_count/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_toss_win_count(name):
    var = np.array(ipl_matches_array[:,[0,5]])
    return np.count_nonzero(np.unique(var[np.array([myfunc(row,name) for row in var])][:,[0]]))

def myfunc(row,name):
    return row[1] == name

# count = get_toss_win_count(b'Mumbai Indians')
# print(count)
# print(np.array(ipl_matches_array[:,[0,5]]))


