import requests
from requests.exceptions import HTTPError

ip_address = input("Please enter your ip_address: ")
url = f"https://get.geojs.io/v1/ip/geo/{ip_address}.json"

try:
    resp = requests.get(url)  
    resp.raise_for_status()
    data = resp.json()
    city = data["city"]
    location_url =f"https://www.metaweather.com/api/location/search/?query={city}"
    resp2= requests.get(location_url)
    resp2.raise_for_status()
    if len(resp2.json()) > 0:
        loc = resp2.json()[0]["woeid"]
        weather_url = f"https://www.metaweather.com/api/location/{loc}/"
        resp3 = requests.get(weather_url) 
        resp3.raise_for_status()
        weather = resp3.json()["consolidated_weather"][0]["weather_state_name"]
        print("The weather on your place: "+ weather)
    else:
        print("Sorry, your city (" + city + ") is not in the database.")

except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
except Exception as err:
        print(f'Other error occurred: {err}')  
else:
        print('Success!')
    
