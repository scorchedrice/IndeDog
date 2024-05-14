import requests
from bs4 import BeautifulSoup
import pprint
import json
import re

movie_data = []

url = 'http://www.indieseoul.org/movie_info/movie_index.php?cate=0'
default_img_url = 'http://www.indieseoul.org'
response = requests.get(url, verify=False)
cnt = 0
id = 10000

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    detail = soup.select('ul.movies > li')
    imgs = soup.select('ul.movies > li > div.img_box > div.img')
    # detail = [v for v in detail if v ]
    for i in range(4):
        temp = detail[i].text.split('\n')
        temp = [v for v in temp if v and v != '\r']
        temp2 = str(imgs[i])
        start = temp2.find("(")
        end = temp2.find(")")
        result = temp2[start+1:end]
        pprint.pprint(temp)
        print(result)
        movieInfo = {
                "model": "movies.movie",
                "pk": id,
                "fields": {
                    'title': temp[0],
                    'img_src': re.sub(r'&amp;', '&', default_img_url + result),
                }
            }
        movie_data.append(movieInfo)
        id += 1
else : 
    print(response.status_code)
  
with open("movie_data2.json", "w", encoding='utf-8') as f:
    json.dump(movie_data, f, indent=2, ensure_ascii=False)
