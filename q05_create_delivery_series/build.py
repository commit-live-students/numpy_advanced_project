#Default Imports
import pandas as pd
import numpy as np
from pandas import Series
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")

def create_delivery_series():
    a = ipl_matches_array
    return Series(a[:,11])

print create_delivery_series()
