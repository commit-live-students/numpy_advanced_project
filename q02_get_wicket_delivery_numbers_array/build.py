# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

#Your Solution

def get_wicket_delivery_numbers_array(batsman):

    wkt_delv=[]
    for x in ipl_matches_array:
        if x[20]==batsman:
            wkt_delv.append(x[11])
              
    #print (wkt_delv)
    return wkt_delv

#get_wicket_delivery_numbers_array(b'ST Jayasuriya')


