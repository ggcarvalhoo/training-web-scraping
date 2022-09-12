"""
1- Entre no site Scrape this site e imprima a mensagem principal no body da página.
OBS: Para conseguir realizar a requisição da página, você deve trabalhar com headers.
Entenda como seu navegador faz a chamada da página, os headers utilizados e reproduza.
"""

import requests
from bs4 import BeautifulSoup

url = 'http://www.scrapethissite.com/pages/advanced/?gotcha=headers'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

