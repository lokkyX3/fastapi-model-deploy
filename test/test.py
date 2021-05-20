import pandas as pd
import numpy as np
import random
import json
import requests

df = pd.read_csv('test.csv')

random.seed(101)
random_ind = random.randint(0,len(df))
new_customer = df.drop('loan_repaid',axis=1).iloc[random_ind]
print(new_customer)
url = 'http://localhost/predict-post/'
data = json.dumps(new_customer.tolist())

resp = requests.post(url, json=data)
print(resp.json())