import requests
from bs4 import BeautifulSoup

url = "https://www.vg.no"
response = requests.get(url)
html = response.content
overskrifter = []

soup = BeautifulSoup(html, 'html.parser')

titles = soup.find_all(['h1','h2','h3','h4','h5','h6'])
for title in titles:
    overskrifter.append(title.text)