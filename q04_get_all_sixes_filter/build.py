# %load q04_get_all_sixes_filter/build.py
#Default Imports
import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_all_sixes_filter():
    def sixtrue(value):
        if value==6:
            return True
        else:
            return False

    
    data_df=pd.read_csv('data/ipl_matches_small.csv')
    value = data_df['runs'].apply(sixtrue)
    return value

#Your Solution


import numpy as np
import pandas as pd
ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
def get_all_sixes_filter():
    def sixtrue(value):
        if value==6:
            return True
        else:
            return False

    
    data_df=pd.read_csv('data/ipl_matches_small.csv')
    value=data_df['runs'].apply(sixtrue)
    return value

get_all_sixes_filter()

