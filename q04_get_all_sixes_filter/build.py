# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')


#Your Solution
def get_all_sixes_filter():
    #ipl_matches_array[0][16]
    list_of_runs = []
    rows = ipl_matches_array.shape[0]
    for i in range(0,rows):
        if int(ipl_matches_array[i][16]) == 6:
            list_of_runs.append(True)
        else:
            list_of_runs.append(False)
        #list_of_runs.append(int(ipl_matches_array[i][16]))
    #print(list_of_runs)  
    return np.array(list_of_runs)





