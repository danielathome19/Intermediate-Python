import os
import requests
from dotenv import load_dotenv

load_dotenv()

zip_code = input("Enter your zip code: ")

headers = {'User-Agent': os.environ["NWS_USER_AGENT"]}
# .environ throws KeyError, .getenv does not

try:
    zip_url = f"https://api.zippopotam.us/us/{zip_code}"
    zip_res = requests.get(zip_url).json()

    place = zip_res['places'][0]
    lat, lon = place['latitude'], place['longitude']
    print(f"Weather for {place['place name']}, {place['state']}:")

    loc_url = f"https://api.weather.gov/points/{lat},{lon}"
    loc_res = requests.get(loc_url, headers=headers).json()

    fc_url = loc_res['properties']['forecast']
    fc_res = requests.get(fc_url, headers=headers).json()

    forecast = fc_res['properties']['periods'][0]
    print(str(forecast['temperature']) + forecast['temperatureUnit'])
    print(forecast['detailedForecast'])
except Exception as e:
    print("Error:", e)