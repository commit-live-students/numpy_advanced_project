import pandas as pd

def create_runs_series(match_code):
    match_code=int(match_code)
    ipl_data=pd.read_csv('./data/ipl_matches_small.csv',index_col='delivery')
    runs_series=ipl_data[ipl_data['match_code']==match_code]['runs']
    return runs_series
ans=create_runs_series('392203')
ans

