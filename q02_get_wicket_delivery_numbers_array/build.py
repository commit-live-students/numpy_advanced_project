# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    wicket_delivery=np.array('')
    for data in ipl_matches_array:
        #print(data[-3])
        if batsman in str(data[-3]) :
            #print(data[-3])
            wicket_delivery=np.append(wicket_delivery,data[-12])
    return(wicket_delivery[1:])        
    
    
    
#get_wicket_delivery_numbers_array('ST Jayasuriya')


