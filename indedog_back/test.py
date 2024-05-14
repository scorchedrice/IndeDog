import requests
from bs4 import BeautifulSoup
import pprint
import json
import re

movie_data = []
i = 4624

while i <4626:
  url = f'https://indieground.kr/indie/movieLibraryView.do?seq={i}&type=D'
  response = requests.get(url, verify=False)
  cnt = 0
  
  if response.status_code == 200:
      html = response.text
      soup = BeautifulSoup(html, 'html.parser')
      if soup.select_one('h2.subject'):
        print(i)
        title = soup.select_one('h2.subject').text.split('\n')[0]
        # director = soup.select_one('div.detail')
        # print(director)
        explain = soup.select_one('div.explain > ul.cf').text.split('\n')
        title_en = explain[1]
        making_year = explain[2]
        genre = explain[3]
        length = explain[4] + explain[5].strip('\t')
        detail = soup.select_one('div.detail').text.split()
        director = ''
        keywords = ''
        age = ''

        for el in explain:
            if '관람가' in el:
                age = el.strip('\t')

        for el in detail:
            if el == '감독':
                cnt = 1
                continue
            elif '#' in el:
                keywords += el
            elif el == '출연' or el == '키워드':
                cnt = 0

            if cnt == 1:
                director += el

        movieInfo = {
            "model": "movies.movie",
            "pk": i,
            "fields": {
                'age': age,
                'genre': genre,
                'title': title,
                'title_en': title_en,
                'director': director,
                'keywords': keywords,
                # 'making_year': making_year,
                # 'length': length,
                'img_src': 'https://indieground.kr'+soup.select_one('div.movie_info_poster > img')['src'],
                'detail': json.dumps(soup.select_one('div.detail').text.split(), ensure_ascii=False)
            }
        }
        movie_data.append(movieInfo)
        pprint.pprint(movieInfo)
  else : 
      print(response.status_code)
      break
  
  i += 1
  
with open("movie_data2.json", "w", encoding='utf-8') as f:
    json.dump(movie_data, f, indent=2, ensure_ascii=False)
