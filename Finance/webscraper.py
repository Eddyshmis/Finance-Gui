import requests
from bs4 import BeautifulSoup
URL = 'https://www.newegg.com/p/32N-0026-007T1?Item=9SIA4REFNE3000&Description=keycaps&cm_re=keycaps-_-9SIA4REFNE3000-_-Product&cm_sp=SP-_-533388-_-0-_-2-_-9SIA4REFNE3000-_-keycaps-_-keycaps-_-1'
Website = requests.get(URL)
soup = BeautifulSoup(Website.content, 'html.parser')
Text_websites = soup.find_all('p')

print()