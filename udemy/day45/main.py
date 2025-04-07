from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://www.youtube.com/")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
content = soup.select("div.content")
for i in content:
    print(i)
'''
movies = soup.select("div.article-title-description__text h3.title")
movies = movies[::-1]
for movie in movies:
    print(movie.text)
'''
# TODO yet to be done as spotipy is not understood yet
