import numpy as np
import pandas as pd
from nba_api.stats.endpoints import LeagueDashPlayerStats

# Extract data using nba_api
def DataExtract(features: list, season_from: int):
    '''
    features: the list of column names you want to extract
    season_from: start season of dataset used to learn ML model
    '''
    df = pd.DataFrame()

    for year in np.arange(season_from,2023):
        season = str(year) + '-' + str((year + 1) % 100).zfill(2)
        # Limit the period to calculate stats so that it is before All-Star
        date_from = str(year) + '-10-01'
        date_to = str(year + 1) + '-01-23'

        df_season = LeagueDashPlayerStats(season=season, per_mode_detailed='Totals', 
                                          date_from_nullable=date_from, date_to_nullable=date_to, 
                                          league_id_nullable='00', season_segment_nullable='Pre All-Star', timeout=100).get_data_frames()[0]
        df_season = df_season[df_season['FG3M_RANK']<=150] # Limit the dataset to purify it
        df_season = df_season.sort_values('FG3_PCT_RANK')[features]
        
        df_season['Season'] = season

        df = pd.concat([df, df_season])

    return df


if __name__ == '__main__':
    features = ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'W_PCT', 
            'MIN', 'FG3M', 'FG3A', 'FG3_PCT', 'PTS', 'PLUS_MINUS', 'NBA_FANTASY_PTS']
    season_from = 2010
    DataExtract(features, season_from)


