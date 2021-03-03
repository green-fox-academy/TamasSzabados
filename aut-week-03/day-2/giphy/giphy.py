import requests
from requests.exceptions import HTTPError

import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('PROJECT_API_KEY')

query = input("Please enter the search word: ")
url = f"https://api.giphy.com/v1/gifs/search?api_key={API_KEY}&q={query}&limit=16&offset=0&rating=g&lang=en"

try:
    resp = requests.get(url)  
    resp.raise_for_status()
    data = resp.json()["data"]
    lines = []
    for i in data:
        lines.append("<img src=" +i["images"]["original"]["url"]+" width='500' height='600'>" +"\n")

    with open("main.html", 'w+') as f:
        f.writelines(lines)
    
except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
except Exception as err:
        print(f'Other error occurred: {err}')  
else:
        print('Success!')