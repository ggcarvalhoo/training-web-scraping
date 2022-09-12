import requests
from bs4 import BeautifulSoup

url = 'https://www.globo.com/'
response = requests.get(url)
soup_instance = BeautifulSoup(response.content, 'html.parser')
menu_items = soup_instance.find_all('span', attrs={'class': 'menu-item-title'})
for item in menu_items:
  print(item.text)

# soup.div - returns first <div> tag
""" 
firstdiv = soup_instance.div
print(firstdiv)
"""

#soup.find('div') also returns first 'div' tag
"""
firstdiv = soup_instance.find('div') 
print(firstdiv)
"""

# .find() method arguments

"""
1- find first ocurrence of a tag:
find(tag)

2- find first ocurrence of a tag,
matching on an attribute-value combo:
ex: find(tag, {attribute:value}) or  find('span', attrs={'class': 'menu-item-title'})
                                                          attribute | content of attribute
"""