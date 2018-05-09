from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
import numpy as np
import pandas as pd
path  = 'data/ipl_matches_small.csv'

def get_total_deliveries_played(batsman):
    ipl_data = np.genfromtxt(path, dtype='|S50', skip_header=1, delimiter=',')
    deliveries = ipl_data[:,13].astype(str)
    deliveries = deliveries[deliveries==batsman]
    return deliveries.size

get_total_deliveries_played('SR Tendulkar')



