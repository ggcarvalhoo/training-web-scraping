import requests
from bs4 import BeautifulSoup

url = 'https://www.globo.com/'
response = requests.get(url)
soup_instance = BeautifulSoup(response.content, 'html.parser')
print(soup_instance.title.string)