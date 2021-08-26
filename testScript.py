# This is a test script. The goal is to get a connection with an API.

import requests

# send GET request to JSONPlaceholder
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()