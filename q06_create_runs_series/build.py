#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


def create_runs_series(match_code):
    c = (ipl_matches_array[:,0] == match_code)
    d = ipl_matches_array[:,:][c]
    b = pd.Series(d[:,16],index=d[:,11])

    return b
