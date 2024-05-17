import requests
from bs4 import BeautifulSoup
import pprint
import json
import re


model = "movies.cinema.recent_movies"

with open("movie_data2.json", "r", encoding='utf-8') as f:
    data_movie = json.load(f)

with open("cinema_data.json", "r", encoding='utf-8') as f:
    data_cinema = json.load(f)


id = 1
recent_movies_list = []
for cinema in data_cinema:
    for movie in data_movie:
        cinemas = movie['fields']['cinemas'].split(',')
        if cinema['fields']['address'] in cinemas:
            recent_movies = {
              'model': model,
              'pk': id,
              'fields': {
                'cinema': cinema['pk'],
                'movie': movie['pk'],
              }
            }
            id += 1
            recent_movies_list.append(recent_movies)


with open("cinema_movie_data.json", "w", encoding='utf-8') as f:
    json.dump(recent_movies_list, f, indent=2, ensure_ascii=False)

pprint.pprint(recent_movies_list)