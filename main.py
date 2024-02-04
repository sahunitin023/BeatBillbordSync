import requests
from bs4 import BeautifulSoup

date = input("Which year you would like to travel to in YYY-MM-DD format: ")
response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}/')
response.raise_for_status()
contents = response.text
# print(contents)
soup = BeautifulSoup(contents, 'html.parser')
top_songs = [tag.getText().strip() for tag in soup.select("li ul li h3")]
