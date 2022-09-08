import requests
import json

URL=('https://v3.football.api-sports.io/leagues?' 'name=premier league')

header = {
    'x-rapidapi-host': 'https://v3.football.api-sports.io',
    'x-rapidapi-key': '8c50abd110875d931db77816c10de961'
}
response = requests.request("GET", URL, headers=header).json()
print(json.dumps(response, indent=4))
