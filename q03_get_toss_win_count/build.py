
from greyatomlib.numpy_advanced.q01_get_total_deliveries_players.build import ipl_matches_array
import numpy as np
import pandas as pd
from pandas import DataFrame

def get_toss_win_count(team):
	alltoss = DataFrame(ipl_matches_array)
	tosswon = alltoss[alltoss[5]== team]
	count = len(tosswon.groupby(by=0).count())
	return count

print get_toss_win_count("Mumbai Indians")
