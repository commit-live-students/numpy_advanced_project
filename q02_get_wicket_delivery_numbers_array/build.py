# %load q02_get_wicket_delivery_numbers_array/build.py
#Default Imports
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

player_out=ipl_matches_array[:,20]
#Your Solution
def get_wicket_delivery_numbers_array(player_out):
    delivery= np.array([])
    for i in range(ipl_matches_array.shape[0]):
        if (player_out[i]):
            delivery=np.append(delivery,ipl_matches_array[:,11][i])
        else:
            pass
    return delivery


get_wicket_delivery_numbers_array(player_out)
if(player_out[21]):
    print(player_out[21])
deliveries[21]
range(ipl_matches_array.shape[0])

np.append(delivery,player_out[2])

for i in range(ipl_matches_array.shape[0]):
        if (player_out[i]):
            np.append(delivery,ipl_matches_array[:,11])
        else:
            pass
for i in range(30):
        if (player_out[i]):
            np.append(delivery,deliveries[i])
            
delivery
delivery= []
delivery= np.array(delivery)
delivery.shape

