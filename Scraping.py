import urllib.request
import json
from bs4 import BeautifulSoup
from requests import get
from urllib.request import Request, urlopen

req = Request(
    url='https://casadosdados.com.br/solucao/cnpj/l-c-pires-eireli-32903305000108', 
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = urlopen(req).read()
#req = get('https://casadosdados.com.br/solucao/cnpj/l-c-pires-eireli-32903305000108')
#result = req.text
url = webpage
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html5lib')
list_item = soup.find('div', attrs={'class': 'columns'})
name = list_item.text.strip()
print(name)