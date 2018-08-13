# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")


#Your Solution
def get_all_sixes_filter():
    six_filter = []
    for i in ipl_matches_array:
        if i[16] == '6':
            six_filter.append(True)
        else:
            six_filter.append(False)
    actual_filter = np.array(six_filter)
    return actual_filter

actual_filter = get_all_sixes_filter()
