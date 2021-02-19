from lxml import html
import numpy as np 
import pandas as pd

with open("leviatan.html", "r",encoding="utf8") as f:
    tree = html.parse(f)
    print(tree)

    #getting genres
    genres = tree.xpath('/html/body/div[2]/div[3]/div[1]/div[2]/div[5]/div[7]/div/div[2]/div/div/div/a[1]/text()')
print(genres)

genres_dict ={}

for i in range(0,len(genres)-1,2):
    genres_dict[genres[i]] = genres[i+1]

genres_series = pd.Series(genres_dict)
df = pd.DataFrame(genres_series)
df.to_csv('out.csv')


