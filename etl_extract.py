# !pip install kaggle # Instala a biblioteca do Kaggle
import kaggle
import pandas as pd
import os

# os.environ['KAGGLE_CONFIG_DIR'] = './pythonProject1'

# Autentica a API do Kaggle
kaggle.api.authenticate()
insertData = "ethanchen44/nba-playoff-predictions"

# Baixa o conjunto de dados (dataset) desejado
kaggle.api.dataset_download_files(insertData, unzip=True)

# Lê o arquivo CSV baixado com o pandas
games = pd.read_csv('nba_games.csv')
playoffs = pd.read_csv('nba_playoffs.csv')

# Exibe as primeiras linhas do dataframe
# print(games.head())
print('-------------------------')
print(playoffs.head())

dfTotal = games
dfTotal["playoffs_team"] = playoffs["team"]
dfTotal["playoffs_team_short"] = playoffs["team_short"]
dfTotal["playoffs_seed"] = playoffs["seed"]
dfTotal["conference"] = playoffs["conference"]
dfTotal.to_csv('nba.csv')
print('-------------------------')
print(dfTotal.head())

