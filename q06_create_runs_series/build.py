#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd


#Your Solution

def create_runs_series(match_code):

    matchcode = ipl_matches_array[:,0]
    delivery = pd.Series(ipl_matches_array[:,11])
    run = pd.Series(ipl_matches_array[:,16], index = delivery)
    runs = run[matchcode == match_code]
    #print delivery
    #print runs

    #columns = ['delivery','match_code','runs']
    #data = matchcode[match_code].pd.Series(runs, delivery)

    return runs
