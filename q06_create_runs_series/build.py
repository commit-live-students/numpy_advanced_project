# %load q06_create_runs_series/build.py
#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd

match = ipl_matches_array[:,[0,11,16]]
delivery = pd.Series(match[:,1])
def create_runs_series(match_code):
    df =  pd.DataFrame(data = match,index = delivery)
    new_df = df[df.iloc[:,0] == match_code]
    runs = new_df.iloc[:,2]
    return runs
#Your Solution
