# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    batsman_dict = dict()

    for row in list(ipl_matches_array[ipl_matches_array[:,-3].astype(str)!=''][:,[-3,11]].astype(str)):
        if row[0] in batsman_dict:
            batsman_dict[row[0]].append(float(row[1]))
        else:
            batsman_dict[row[0]] = [float(row[1])]
    return np.array(batsman_dict[batsman])



