import requests
from requests.exceptions import HTTPError

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('PROJECT_API_KEY')

query = "Apollo 11"
url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json?q={query}&api-key={API_KEY}"

try:
    
    resp = requests.get(url)  
    resp.raise_for_status()
    data = resp.json()["response"]["docs"]
    for i in data:
        list1 = []
        list1.append(i["lead_paragraph"])
        list1.append(i["snippet"])
        list1.append(i["pub_date"])
        print(list1)

   

except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
except Exception as err:
        print(f'Other error occurred: {err}')  
else:
        print('Success!')

