# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
ipl=[]
for x in ipl_matches_array[:,11:21]:
    ipl.append(x)  
    
#Your Solution
def get_wicket_delivery_numbers_array(batsman):
    delivery = []
    for x1 in ipl:
        if x1[9]==batsman:
            delivery.append(x1[0])
    
    return delivery
    


get_wicket_delivery_numbers_array(b'ST Jayasuriya')

    




