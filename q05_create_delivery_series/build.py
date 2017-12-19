from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
#ipl_matches_array = np.genfromtxt("data/ipl_matches_small.csv",dtype="|S50", delimiter=",")

def create_delivery_series():
    delivery = pd.Series(ipl_matches_array[:, 11])
    return (delivery)


print create_delivery_series()
