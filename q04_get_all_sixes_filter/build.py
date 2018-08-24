# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    batsmen = [];
    for i in range(len(ipl_matches_array)):
        batsmen.append(np.int(ipl_matches_array[i][16]) ==  6)
    return batsmen
expected_filter = (ipl_matches_array[:, 16].astype(np.int16) == 6)
actualfilter = get_all_sixes_filter()
np.all(expected_filter == actualfilter)


