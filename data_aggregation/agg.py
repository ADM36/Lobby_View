import requests, json
import pandas as pd
from pandas.io.json import json_normalize

# query = {"legal_name": "Microsoft Corp"}
query = {}

results = requests.post('https://www.lobbyview.org/public/api/reports', data = json.dumps(query), verify=False)

# print(results.json())

json_object = results.json() 

df = json_normalize(json_object['result'])

print(df.head())

df.to_csv('visualization/LobbyView'+'.csv')
