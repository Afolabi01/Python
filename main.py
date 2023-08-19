import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/forms/'

my_page = requests.get(url)

soup = BeautifulSoup(my_page.text, 'html.parser')
