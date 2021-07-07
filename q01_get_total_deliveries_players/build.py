
import numpy as np 
def get_total_deliveries_played(batsman):
        ipl_matches = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
        deliveries = ipl_matches[:,13].astype(np.str)
        deiveries_batsman = deliveries[deliveries == batsman]
        deliveries_total = deiveries_batsman.size
        return deliveries_total
get_total_deliveries_played('SR Tendulkar')


