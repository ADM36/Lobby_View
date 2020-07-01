import requests, json
# import pandas as pd
# from pandas.io.json import json_normalize

with open('companies.csv','r') as co_file:
    next(co_file)
    for row in co_file:
        legal_name = row.strip()

        for i in range(2010,2019):

            query = {"legal_name": legal_name, "year":i} #alternatively, could do "year":{"lt":"2019","gte":"2010"} 

            results = requests.post('https://www.lobbyview.org/public/api/reports', data = json.dumps(query), verify=False)


            json_object = results.json()

            with open(f"./data_aggregation/{legal_name}_{i}.json", "w") as write_file:
                json.dump(json_object, write_file)
