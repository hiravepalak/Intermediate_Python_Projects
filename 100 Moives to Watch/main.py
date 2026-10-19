import requests
from bs4 import BeautifulSoup
import lxml

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Scrape the website and store all the movies in a list
soup = BeautifulSoup(requests.get(URL).content, 'lxml')

movie_list = [h3.get_text(strip=True) for h3 in soup.find_all("h3", class_="title")]

ordered_movie_list = []
for movie in reversed(movie_list):
    ordered_movie_list.append(movie)

with open("movies.txt", "w", encoding="utf-8") as file:
  for movie in ordered_movie_list:
    file.write(movie + "\n")
