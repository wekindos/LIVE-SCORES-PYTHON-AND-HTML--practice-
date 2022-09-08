from email import header
from urllib import request, response
import requests
import json

url= ('https://v3.football.api-sports.io/teams?' 'league=39&' 'season=2019')
header ={
    'x-rapidapi-host':"v3.football.api-sports.io",
    'x-rapidapi-key':'8c50abd110875d931db77816c10de961'
}

response = requests.request("GET", url, headers=header).json()
print(json.dumps(response, indent=4))