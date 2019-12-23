import pandas as pd

def get_all_sixes_filter() :
   # team=team.decode('ASCII')
    ipl_matches_array =pd.read_csv('data/ipl_matches_small.csv')
    sixs=(ipl_matches_array['runs']==6)
    #expected_filter = (ipl_matches_array[:, 16] == 6)
    #print(expected_filter)
    #&(df['toss_decision']!='bat')
    return sixs

print(get_all_sixes_filter())


