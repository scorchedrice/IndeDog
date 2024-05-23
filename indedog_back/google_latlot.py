import requests
from bs4 import BeautifulSoup
import pprint
import json
import re

# 구글 지도 API를 이용한 상영관 좌표 불러오기

address = '서울특별시교육청 강서도서관'
api_key = 'AIzaSyB4iMRT75dIyGna5K1Rq9MSr6X7eUm-__E'

with open("movie_data2.json", "r", encoding='utf-8') as f:
    data = json.load(f)

def get_geocode_info(address, api_key):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get("results"):
            result = data["results"][0]
            formatted_address = result.get("formatted_address")
            location = result.get("geometry", {}).get("location", {})
            latitude = location.get("lat")
            longitude = location.get("lng")
            return {
                "formatted_address": formatted_address,
                "latitude": latitude,
                "longitude": longitude
            }
    return None

# model = "movies.cinema.recent_movies"

cinemaList = []
cinemaResult = []
cinema_id = 1
for i in range(4):  
  cinemas = data[i]['fields']['cinemas'].split(',')
  for cinema in cinemas:
      print(cinema)
      if cinema == '':
          continue
      if cinema not in cinemaList:
          if cinema == '강서도서관':
              result = get_geocode_info('서울특별시교육청 ' + cinema, api_key)
          else:
            result = get_geocode_info(cinema, api_key)
          cinemaList.append(cinema)
          cinemaInfo = {
                "model": "movies.cinema",
                "pk": cinema_id,
                "fields": {
                    "address": cinema,
                    "latitude": result['latitude'],
                    "longitude": result['longitude']
                }
            }
          cinema_id += 1
          cinemaResult.append(cinemaInfo)

pprint.pprint(cinemaResult)

with open("cinema_data.json", "w", encoding='utf-8') as f:
    json.dump(cinemaResult, f, indent=2, ensure_ascii=False)