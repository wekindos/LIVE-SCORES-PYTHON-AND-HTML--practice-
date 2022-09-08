from urllib import response
import requests
import json

url = ('https://v3.football.api-sports.io/fixtures/rounds?' 'season=2022&' 'league=39&' 'current=FALSE')

header ={
    'x-rapidapi-host': "https://v3.football.api-sports.io",
    'x-rapidapi-key':"8c50abd110875d931db77816c10de961"
}
response = requests.request("GET", url, headers=header).json()
print(json.dumps(response, indent=4))