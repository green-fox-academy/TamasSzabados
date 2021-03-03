import requests
from requests.exceptions import HTTPError

query = input("Please enter a character name: ")
url = f"https://swapi.dev/api/people/?search={query}"

try:
    
    resp = requests.get(url)  
    resp.raise_for_status()
    data = resp.json()["results"]
    print(data[0]["name"])
    print(data[0]["height"])
    print(data[0]["mass"])
    print(data[0]["hair_color"])
    print(data[0]["skin_color"])
    print(data[0]["eye_color"])

except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
except Exception as err:
        print(f'Other error occurred: {err}')  
else:
        print('Success!')

