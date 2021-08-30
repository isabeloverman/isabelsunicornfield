# author: isabeloverman
# This is a test script. The goal is to get a connection with an API.
# https://www.youtube.com/watch?v=W--_EOzdTHk << good reference

import os
import re
import requests
import argparse

# lines from Byan's code about parsing args that look important
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--username', metavar='email:password', help='Used to make API calls', nargs=1, required=True)
args = parser.parse_args()

#callback url specified when the application was defined
callback_uri = "https://staging-app.infosecinstitute.com"

# get api token from envrionment variable
token = os.environ['api-token']

# send GET request to Skills
api_url = "https://staging-app.infosecinstitute.com/portal/api/v1/learners?limit=2"
response = requests.get(api_url)
response.json()

print(response.json())

# status code for GET
code = response.status_code

response.headers["Content-Type"]

print(response)
print(response.headers["date"]) #shows date and time of request





# GET article URL - does it exist in instance?
req = Request('GET', api_url, headers={'content-type': 'application/json'}, auth=(username, password))
prepped = req.prepare()
resp = s.send(prepped)
if resp.status_code != 200:
    print(f'Error: status code {resp.status_code} getting {api_url}.')
else:
    # Output warning that article's old seciton ID is same as new section ID
    json_data = json.loads(resp.text)







# Regex check username:password.
username_regex = re.compile('\S+:\S+')
match = username_regex.search(args.username[0])
user_credentials = []
if not match:
    print('Error: not a valid user credentials - need username:password')
else:
    user_credentials = args.username[0].split(":")