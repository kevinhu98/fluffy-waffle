import tmdbsimple as tmdb
import json
import pymongo
import os
import requests
from dotenv import load_dotenv

load_dotenv()

tmdb.API_KEY = os.getenv('TMDB_API_KEY')

request_string = 'https://api.themoviedb.org/3/movie/upcoming?api_key=' + tmdb.API_KEY +'&language=en-US&page=1&region=US'

r = requests.get(request_string)

for movie in r.json()['results']:
    print(movie['id'])