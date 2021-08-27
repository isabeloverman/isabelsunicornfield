# This is a test script. The goal is to get a connection with an API.
# https://www.youtube.com/watch?v=W--_EOzdTHk << good reference

#import json
import requests
import argparse

# send GET request to JSONPlaceholder
api_url = "https://staging-app.infosecinstitute.com/portal/api/v1/learners?llimit=2"
response = requests.get(api_url)
response.json()

print(response.json())

# status code for GET
code = response.status_code

response.headers["Content-Type"]

print(response)