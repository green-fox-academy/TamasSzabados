import requests
from requests.exceptions import HTTPError
from lxml import html

try:
    url = "https://en.wikipedia.org/wiki/Red_Hot_Chili_Peppers_discography"
    resp = requests.get(url)  
    resp.raise_for_status()  
    tree = html.fromstring(resp.content)
    album_titles = tree.xpath('/html/body/div[3]/div[3]/div[5]/div[1]/table[2]/tbody/tr/th/i/a/text()')
                               
    for title in album_titles:
        print(title)

except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
#except Exception as err:
        #print(f'Other error occurred: {err}')  
#else:
        #print('Success!')




