"""
1- Entre no site Scrape this site e imprima a mensagem principal no body da página.
OBS: Para conseguir realizar a requisição da página, você deve trabalhar com headers.
Entenda como seu navegador faz a chamada da página, os headers utilizados e reproduza.
"""
import bs4
import requests
from bs4 import BeautifulSoup

url = 'http://www.scrapethissite.com/pages/advanced/?gotcha=headers'
headers = {'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' }
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

rep = soup.find(class_ = "col-md-4 col-md-offset-4").text
print(rep.strip())

