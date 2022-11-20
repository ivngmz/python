import requests
import json
import os

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock market&from=2022-10-27&to=2022-2-28&sortBy=popularity&language=en&apiKey=890603a55bfa47048e4490069ebee18c')

content = r.json()

path_file=os.path.abspath(os.path.join(os.path.dirname(__file__)))
with open(str(path_file) + "/response_from.API.json", "w") as myfile:
    myfile.write(json.dumps(content, indent=4))