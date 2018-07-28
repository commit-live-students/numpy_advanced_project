# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
batsman = b'ST Jayasuriya'
#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    '''
    df = pd.read_csv('data/ipl_matches_small.csv')
    wicket_delivery_numbers_array = df.loc[df['player_out']==batsman]
    return np.array(wicket_delivery_numbers_array['delivery'])
    '''
    arr = ipl_matches_array[:,[11,20]]
    condition = (arr[:,1]==batsman)
    arr_1 = arr[condition]
    return arr_1[:,0]


