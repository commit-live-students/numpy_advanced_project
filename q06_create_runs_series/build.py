#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution
def create_runs_series(match_code):
    delivery,runs=[],[]
    for i in ipl_matches_array[:,[0,11,18]]:
        if(i[0]==match_code):
            delivery.append(i[1])
            runs.append(i[2])
    s=pd.Series(runs,delivery)
    return s
