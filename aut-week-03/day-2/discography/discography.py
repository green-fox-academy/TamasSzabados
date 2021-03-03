import requests
from requests.exceptions import HTTPError
from lxml import html

try:
    url = "https://musicboard.app/artist/182/releases"
    resp = requests.get(url)  
    resp.raise_for_status()  
    tree = html.fromstring(resp.content)
    print(resp.text)
    album_titles = tree.xpath('.//*[@id="root"]/div/div/div/div[3]/div[2]/div[1]/div[1]/div[2]/div[4]/a/div/h6//text()')
    print(album_titles)

  
    #for title in album_titles:
        #print(title)

except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  
#except Exception as err:
        #print(f'Other error occurred: {err}')  
#else:
        #print('Success!')




