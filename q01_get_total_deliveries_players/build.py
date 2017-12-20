import numpy as np
import pandas as
from pandas import Series, DataFrame
ipl_matches_array = np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')
# Your Solution
def get_total_deliveries_played(batsman = 'SR Tendulkar'):
    batsman1 = DataFrame(ipl_matches_array[:, 13:14])
    count1 = DataFrame(batsman1)
    count1.columns = ['name']
    count_deliveries = count1.name.value_counts()[batsman]
    #print type(count_deliveries)
    return count_deliveries

print get_total_deliveries_played(batsman = 'SR Tendulkar')




