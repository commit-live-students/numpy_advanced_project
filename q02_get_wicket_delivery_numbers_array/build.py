# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

#Your Solution
def get_wicket_delivery_numbers_array (player):
    ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='S50', skip_header=0, delimiter=',')
    deliveries_col_no = 0
    player_out_column_no = 0
    delivery_list = []
    
    head = list(enumerate(ipl_matches_array[0]))
    
    #to get column numbers
    for x in range (0,len(head)):
        if head[x][1] == 'player_out':
            player_out_column_no = x
        elif head[x][1] == 'delivery':
            deliveries_col_no = x
            
    ipl_matches_array_new = ipl_matches_array[1:]
    
    for x in range(0,len(ipl_matches_array_new)):
        if ipl_matches_array_new[x,[player_out_column_no]][0] == player:
            delivery_list.append(ipl_matches_array_new[x,[deliveries_col_no]][0])
    
    np_array = np.array(delivery_list)
    return np_array



