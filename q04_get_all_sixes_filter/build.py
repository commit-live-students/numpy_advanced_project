
import numpy as np

ipl_matches_array =np.genfromtxt('data/ipl_matches_small.csv', dtype='|S50', skip_header=1, delimiter=',')

# Your Solution
def get_all_sixes_filter():
    run_scored = ipl_matches_array[:, 16] == (b'6')
    print (run_scored)
    return run_scored
get_all_sixes_filter()


