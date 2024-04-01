import math
import statistics
import sympy
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from sklearn import datasets
import random
import seaborn as sns
from scipy.stats import chi2_contingency
from dython.nominal import associations
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import PowerTransformer, StandardScaler
from sklearn.compose import make_column_selector
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import statsmodels.api as sm
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time 
import requests
import json
from bs4 import BeautifulSoup


year_list = list(range(2014, 2024, 1))
data_all_years = []
match_ids = []
home_team = []
away_team = []
home_goals = []
away_goals = []
home_xG = []
away_xG = []
datetime = []
for year in year_list:
    url = f"https://understat.com/league/EPL/{year}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    scripts = soup.find_all('script')
    strings = scripts[1].string
    ind_start = strings.index("('") + 2
    ind_end = strings.index("')")
    json_data = strings[ind_start : ind_end]
    json_data = json_data.encode('utf8').decode('unicode_escape')
    data = json.loads(json_data)
    for match in data:
        if match['isResult']:  
            match_ids.append(match['id'])
            home_team.append(match['h']['title'])
            away_team.append(match['a']['title'])
            home_goals.append(match['goals']['h'])
            away_goals.append(match['goals']['a'])
            home_xG.append(match['xG']['h'])
            away_xG.append(match['xG']['a'])
            datetime.append(match['datetime'])

df_matches = pd.DataFrame({
    'Match ID': match_ids,
    'Home Team': home_team,
    'Away Team': away_team,
    'Home Goals': home_goals,
    'Away Goals': away_goals,
    'Home xG': home_xG,
    'Away xG': away_xG,
    'Datetime': datetime
})

df_matches.to_csv('PL_match_data.csv', index=False)