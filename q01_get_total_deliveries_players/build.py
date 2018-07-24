# # %load q01_get_total_deliveries_players/build.py
# # Default imports
# import numpy as np


# def get_total_deliveries_played(batsman):
#     ipl_matches=np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')    
#     ball_deliveries=ipl_matches[:,13]
#     if(deliveries==batsman):
#         uniue_balls=np.unique(batsman_deliveries, return_counts=Tru
#     return (zip(uniue_balls))[True]
# def get_total_deliveries_played(batsman):
#     batsman = str.encode(batsman)
#     ipl_matches = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
#     deliveries = ipl_matches[:,13]
#     batsman_d = (deliveries == batsman)
#     unique, counts = np.unique(batsman_d), return_counts=True)
#     return dict(zip(unique, counts))[True]
# get_total_deliveries_played()
# import numpy as np

# def get_total_deliveries_played(batsman):
#     #Loads the data and then access the column named as batsman.
#     batsman = str.encode(batsman)
#     matches_a = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
#     deliveries = matches_a[:,13]
#     #Calculates the total no. of occurences of the particular batsman(
#     batsman_deliveries = (deliveries == batsman)
#     #particular batsman(user given) in order to give the deliveries.
#     unique, counts = np.unique(batsman_deliveries, return_counts=True)
    
#     return dict(zip(unique, counts))[True]

 
# get_total_deliveries_played(batsman)

# import numpy as np
# def get_total_deliveries_played(batsman):
#     batsman = str.encode(batsman)
#     ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
#     deliveries = ipl_matches_array[:,13]
#     batsman_deliveries = (deliveries == batsman)
#     unique, counts = np.unique(batsman_deliveries, return_counts=True)
#     return dict(zip(unique, counts))[True]
# get_total_deliveries_played('RT Pointing')
# import numpy 
# ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# def get_total_deliveries_played(batsman):
#     batsman_deliveries =  ipl_matches_array[ipl_matches_array[:,13] == batsman]
#     return len(batsman_deliveries)
# get_total_deliveries_played(batsman)

import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_total_deliveries_played(batsman):
    unique, counts = np.unique(ipl_matches_array[:,13], return_counts=True)
    batsman_count=dict(zip(unique,counts))
    return int(batsman_count[batsman])

# import numpy as np

# ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# # Your Solution
# def get_total_deliveries_played(batsman):
#     unique, counts = np.unique(ipl_matches_array[:,13], return_counts=True)
#     batsman_count=dict(zip(unique,counts))
#     return int(batsman_count[batsman])

get_total_deliveries_played


