import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from DataExtract import *
from ContestParticipants import *

# feature values
features = ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP', 'W_PCT', 
            'MIN', 'FG3M', 'FG3A', 'FG3_PCT', 'PTS', 'PLUS_MINUS', 'NBA_FANTASY_PTS']

# feature values (Rank ver.) 
features_rank = ['PLAYER_ID', 'PLAYER_NAME', 'TEAM_ABBREVIATION', 'GP_RANK',
                 'W_PCT_RANK', 'MIN_RANK', 'FG3M_RANK', 'FG3A_RANK', 'FG3_PCT_RANK', 
                 'PTS_RANK', 'PLUS_MINUS_RANK', 'NBA_FANTASY_PTS_RANK']

# Import data set between 2012-13 and 2022-23
df = DataExtract(features, 2012)