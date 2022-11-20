import requests
import json

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock market&from=2022-10-27&to=2022-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')

content = r.json()

#parsed = json.loads(r)

#print(json.dumps(content, indent=4))

for article in content["articles"]:
    print(article["description"] + "\n")