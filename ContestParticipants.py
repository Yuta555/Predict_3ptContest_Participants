import pandas as pd
import requests
from bs4 import BeautifulSoup
from nba_api.stats.static import players

# Create a list of 3point Contest participants 
def ContestParticipants():
    # Obtain 3point Contest participants data by screaping
    df = GetDataByScraping()

    # Deal with special case when matching player_id
    df = TreatException(df)

    # Find player ID and create a table of participants
    player_ids = CreateIdList(df)
    
    # Fix and Add each column
    df['Season'] = df['Season'] + '-' + ((df['Season'].astype('int') + 1) % 100).astype('str').str.zfill(2)
    df['Season'] = df['Season'].str.strip()
    df['PLAYER_ID'] = player_ids
    df['Participant'] = 1
    df.drop(columns='PLAYER_NAME', inplace=True)

    return df


# Obtain 3point Contest participants data by screaping
# Use 'RealGM' page
def GetDataByScraping(scrape_page='https://basketball.realgm.com/nba/allstar/three_point/players'):
    r = requests.get(scrape_page)

    # Parsing the HTML
    soup = BeautifulSoup(r.content, 'html.parser')
    
    tbod = soup.find('tbody')
    trs = tbod.find_all('tr')
    sums = 0
    df_players = pd.DataFrame([],columns=['PLAYER_NAME', 'YEAR'], index=range(200))
    for i, tr in enumerate(trs): 
        player = tr.find(attrs={"data-th": "Player"}).text
        year = tr.find(attrs={"data-th": "Year(s)"}).text
        sum = tr.find(attrs={"data-th": "Selections"}).text
        sums += int(sum) # For validation
        df_players.iloc[i, :] = [player, year]

    df_players.dropna(inplace=True)
    df = df_players['YEAR'].str.split(',', expand=True)
    df['PLAYER_NAME'] = df_players['PLAYER_NAME'].str.replace('.', '', regex=False) # Remove the influence on period

    # Transform to the tidy data 
    df = df.melt(id_vars=['PLAYER_NAME']).sort_values(['value']).dropna().reset_index(drop=True)[['value', 'PLAYER_NAME']]
    df.columns = ['Season', 'PLAYER_NAME']
    df['Season'] = (df['Season'].astype('int') - 1).astype('str')

    # Validation
    if sums != len(df):
        print('Error!') 

    return df


# Deal with special case when matching player_id
def TreatException(df):
    # Remove special case "Rimas Kurtinaitis", who was the only European player to participate in the NBA 3Point Contest, 
    # without ever having played in the NBA (according to Wilipedia)
    df = df[df['PLAYER_NAME']!='Rimas Kurtinaitis']

    # Fix player names which don't match with IdList's
    pd.options.mode.chained_assignment = None
    df['PLAYER_NAME'].replace({'Bobby Hansen': 'Bob Hansen',
                               'Cliff Robinson': 'Cliff T Robinson',
                               'Steve Smith': 'Steven Smith',
                               'Roger Mason': 'Roger Mason Jr'}, regex=True, inplace=True)
    
    return df


# Find player ID and create a table of participants
def CreateIdList(df):
    player_ids = []
    for player_name in df['PLAYER_NAME']:
        player_dict = players.get_players()

        # Remove the influence on period
        for item in player_dict:
            item['full_name'] = item['full_name'].replace('.', '')

        player_id = [player for player in player_dict if player['full_name'] == player_name][0]['id']
        player_ids.append(player_id)

    return player_ids


if __name__ == '__main__':
    ContestParticipants()

