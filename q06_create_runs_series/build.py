#Default Imports
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import pandas as pd
import numpy as np

def create_runs_series(match_code):
    runs=[]
    delivery=[]

    for i in ipl_matches_array:
        if i[0]==match_code:
            runs.append(i[16])
            delivery.append(i[11])


    run_series = pd.Series(runs,delivery)
    return run_series




create_runs_series("392203")
