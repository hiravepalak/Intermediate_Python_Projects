import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
response.raise_for_status()
print(response.json()['iss_position']['latitude'], response.json()['iss_position']['longitude'])

""" response codes cheat sheet 
1XX - Hold on (working on it)
2XX - Here you go (everything went well, you should have your data)
3XX - Go away (don't have permission to access)
4XX - You screwed up (client)
5XX - I screwed up (server)
    response.status_code 
    
    find position on map - https://www.latlong.net/Show-Latitude-Longitude.html"""