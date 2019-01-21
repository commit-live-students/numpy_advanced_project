# %load q06_create_runs_series/build.py
#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution


ipl_matches_array[:,11]
def create_runs_series(match_code):
    runs_series = pd.Series()
    list_a = list(ipl_matches_array[:,17])
    #for x in ipl_matches_array[:,11]:
     #   #a = np.array(x)
      #  i = list_a[17].index(x)
       # result = runs_series.append(ipl_matches_array[i,17])
    result = np.array(list_a)
    return result
create_runs_series('392203')
list_a = list(ipl_matches_array[:,17])
list_a[2]
#tmp = ipl_matches_array[:,11] #python list
#a = np.array(tmp) #numpy array
#i = list(a).index(a)    # i will return index of 2, which is 1
#def index(self, ipl_matches_array[:,11]):
 #       return np.where(self == ipl_matches_array[:,11])


