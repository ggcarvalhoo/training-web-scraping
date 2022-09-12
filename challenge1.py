"""
1- Entre no site WebScraper Test
2- Imprima todos os títulos e preços dos laptops disponíveis.
Obs: Esse site possui paginação AJAX, você deve iterar todas as páginas e pegar a informação pedida de todos os itens.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops'
response = requests.get(url)
site = BeautifulSoup(response.text, 'html.parser')

menu_items = site.find_all('div', attrs={'class': 'row ecomerce-items ecomerce-items-ajax'})
print(type(menu_items))

for products in menu_items:
    item = eval(products.attrs['data-items'])
    print(type(item))
    print(len(item))

    names = []
    for title in item:
        names.append(title['title'])

    print(f'Nomes: {names}')
    # for name in names:
    #     print(name)
    #     print(f'titulo: {name}')

    prices = []
    for price in item:
        prices.append(price['price'])

    print(prices)








