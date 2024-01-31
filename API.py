import requests
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

api = os.environ.get('api')
print(api)

url = f"https://newsapi.org/v2/everything?q=\
    accident&from=2024-01-28&sortBy=latest&pageSize=2&apiKey={api}"

response = requests.get(url)
pprint(response.json())
