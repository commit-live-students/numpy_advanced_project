# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=0, delimiter=',')

def get_wicket_delivery_numbers_array(batsman):
    delivery = ipl_matches_array[:,11] # delievery column which has to be given in op is considered as main dataset
    playerout = ipl_matches_array[:,20]==batsman # [create filter: batsman] accesssing the column playerout 
    return delivery[playerout] #apply the filter in the main data(deliveries to get the values)









