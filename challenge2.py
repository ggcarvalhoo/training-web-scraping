"""
1- Entre no site Scrape this site e realize o login.
2- Quando realizado, ele irá mostrar uma mensagem Successfully logged in! Nice job :).
OBS: Qualquer usuário e senha realizará o login, porém existe o desafio de entender como é realizado a requisição para reproduzir no código. Se logado com sucesso, imprima uma mensagem de "Sessão criada"
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/advanced/?gotcha=csrf'

payload = {
    'user': '123',
    'pass': '123',
    'csrf': '404772715',
    'Login →': 'Enviar'
}

# response = requests.get(url, data=payload)
response = requests.post(url, data=payload)
soup = BeautifulSoup(response.text, 'html.parser')

rep = soup.find('div', {"class": "col-md-4 col-md-offset-4"}).text
rep_final = rep.replace('\n', '').strip()

print(rep_final)







