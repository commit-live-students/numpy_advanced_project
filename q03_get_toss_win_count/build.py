
import pandas as pd
def get_toss_win_count(team):
    matches = pd.read_csv('D:/grey work/2ndweekend/data set/ipl_matches_small.csv')
    toss_won_by_team = matches.loc[matches['toss_winner'] == team]
    toss_won_by_team = toss_won_by_team.drop_duplicates('match_code', keep = 'first')
    return toss_won_by_team.shape[0]

