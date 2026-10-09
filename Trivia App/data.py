import requests as rq

# Got API from https://opentdb.com/api_config.php
parameters = {'amount':50, 'type':'boolean'}
response = rq.get("https://opentdb.com/api.php?", params=parameters)
response.raise_for_status()

data = response.json()
question_data = data['results']
