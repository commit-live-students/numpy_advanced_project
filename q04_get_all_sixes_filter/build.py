# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    w=[]   
    rows=ipl_matches_array.shape[0]
    for i in range(0,rows):
        if int(ipl_matches_array[i][16]) == 6:
            w.append(True)
        else:
            w.append(False)
    return np.array(w)






