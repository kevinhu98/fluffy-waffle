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

movies = []

for movie in r.json()['results']:
    movies.append(movie['id'])

#update moviesdb unless already exists with findOne --- https://stackoverflow.com/questions/27482806/check-if-id-exists-in-a-collection-with-mongoose

try:
    client = pymongo.MongoClient("mongodb+srv://kevin:"+os.getenv('MONGO_PW')+"@cluster0.8xh0x.mongodb.net/fluffywaffle.movies?retryWrites=true&w=majority")
    fluffywaffle = client.fluffywaffle
    print('successful connection')
except:
    print('no connection')

for id in movies:
    movie = tmdb.Movies(id)
    data = json.dumps(movie.info(), sort_keys=True, indent=4)
    cleanedData = json.loads(data)
    movieToAdd = {}
    movieToAdd['id'] = cleanedData['id']
    movieToAdd['title'] = cleanedData['title']
    movieToAdd['release_date'] = cleanedData['release_date']
    movieToAdd['poster_path'] = cleanedData['poster_path']
    movieToAdd['overview'] = cleanedData['overview']
    movieToAdd['genres'] = [genre["name"] for genre in cleanedData['genres']]

    movieCollection = fluffywaffle.movies

    if not movieCollection.find_one({"id": movieToAdd['id']}):
        db_id = movieCollection.insert_one(movieToAdd).inserted_id
        print("added " + movieToAdd['title'])
    else:
        print(movieToAdd['title'], " - already exists")

