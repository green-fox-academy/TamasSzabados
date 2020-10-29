# Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
# Also, the URL is missing a crucial component, find out what it is and insert it too!

url = "https//www.reddit.com/r/nevertellmethebots"
url2 = url[:5] + ":" + url[5:38] + "odds"

print(url2)