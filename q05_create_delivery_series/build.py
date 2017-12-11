#Default Imports
import pandas as pd
from pandas import Series
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array

# Using Series function convert the Delivery column from ipl_matches_array into Panda Series
def create_delivery_series():
    variable = pd.Series(ipl_matches_array[:, 11])

    return variable
