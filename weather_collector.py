"""
Script to get weather and asthma real time data and upload to cosmos db.
"""

# import the pymongo library - this is the Python driver!
import pymongo, requests, time 

from secrets import mongo_db_uri 
from secrets import weather_api_key

# db connection to real_time_conditions collection
uri = mongo_db_uri 
client = pymongo.MongoClient(uri)
db = client.pebkacsite
collection = db.real_time_conditions

# using OOP approach for practice
class City:
    def __init__(self, city_name):
        self.city_name = city_name
        self.json_data = None
    
    def get_data(self):
        call_url = f"https://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={self.city_name}&aqi=yes"
        payload = requests.get(call_url)
        self.json_data = payload.json()

# add as required
cities = [City('Sydney'),
          City('Kiama'), 
          City('London'), 
          City('Melbourne'), 
          City('Geelong'),
          City('Beijing'), 
          City('Newcastle Australia'), 
          City('Canberra'), 
          City('Paris'), 
          City('Stockholm'),
          City('Tokyo'),
          City('Los Angeles'),
          City('Moscow')]

# gets and inserts data once every hour
while True:
    insertion_data = []
    for city in cities:
        city.get_data()
        insertion_data.append(city.json_data)
    collection.insert_many(insertion_data)
    time.sleep(3600)





