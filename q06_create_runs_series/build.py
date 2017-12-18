#Default Imports
import pandas as pd
import numpy as np
ipl_matches_array =np.genfromtxt("data/ipl_matches_small.csv", dtype="|S50", skip_header=1, delimiter=",")
def create_runs_series(matchcode):
	subset_array = np.array([[elm[11], elm[16]] for elm in ipl_matches_array if elm[0] == matchcode])
	return pd.Series(subset_array[:,1],index=subset_array[:,0])
