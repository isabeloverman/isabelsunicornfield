# author: isabeloverman
# This is a test script. The goal is to get a connection with the Skills API.
# \/ \/ good references \/ \/
# https://www.nylas.com/blog/use-python-requests-module-rest-apis/#how-to-use-python-requests
# https://www.youtube.com/watch?v=W--_EOzdTHk 

# imports
import os
from requests.auth import HTTPBasicAuth
import requests
import argparse
import json

# getting API key from user input because I can make that work
print("Enter API key:")
api_token = str(input())     # https://www.geeksforgeeks.org/taking-input-from-console-in-python/

# base URL for API
api_url_base =  "http://staging-app.infosecinstitute.com/portal/api/v1/"

# headers: I think the authorization here is wrong or something
headers = {'Content-Type': 'application/json', 'Authorization': '{0}'.format(api_token)}

# call API and get response function
def get_course_info():
    
    api_url = '{0}courses/?limit=2'.format(api_url_base)
    print(api_url)
    response = requests.get(api_url, headers=headers)
    print(headers)
    #print(response.raise_for_status())
    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        print(response.status_code)
        return None

# call function 
course_info = get_course_info()

# check for response information
if course_info is not None:
    print("Here\'s your info")
    #print(course_info)
    for k, v in course_info['courses']:
        print('{0}:{1}'.format(k, v))
        #print('')
else:
    print('[!] Request Failed')





#below this point is previous code that I couldn't get working


# lines from Byan's code about parsing args that look important
#parser = argparse.ArgumentParser()
#parser.add_argument('-u', '--username', metavar='email:password', help='Used to make API calls', nargs=1, required=True)
#args = parser.parse_args()

#callback url specified when the application was defined
#callback_uri = "https://staging-app.infosecinstitute.com"

# get api token from envrionment variable
#token = os.environ['api-token']


# send GET request to Skills
#api_url = "https://staging-app.infosecinstitute.com/portal/api/v1/learners?limit=2"
#my_headers = {'Authorization' : 'Bearer {os.environ[api-token]}'}

#try:
 #   response = requests.get(api_url, auth=(username, token))
  #  print(response.json())

   # response = requests.get(api_url, headers=my_headers)
    #print(response.json())
#except requests.exceptions.HTTPError as errh:
#    print(errh)
#except requests.exceptions.ConnectionError as errc:
#    print(errc)
#except requests.exceptions.Timeout as errt:
#    print(errt)
#except requests.exceptions.RequestException as err:
 #   print(err)

# status code for GET
#code = response.status_code

#response.headers["Content-Type"]

#print(response)
#print(response.headers["date"]) #shows date and time of request



# GET article URL - does it exist in instance?
#req = Request('GET', api_url, headers={'content-type': 'application/json'}, auth=(username, password))
#prepped = req.prepare()
#resp = s.send(prepped)
#if resp.status_code != 200:
#    print(f'Error: status code {resp.status_code} getting {api_url}.')
#else:
    # Output warning that [warning here...]
#    print("Request was a success!")
 #   json_data = json.loads(resp.text)




# Regex check username:password.
#username_regex = re.compile('\S+:\S+')
#match = username_regex.search(args.username[0])
#user_credentials = []
#if not match:
#    print('Error: not a valid user credentials - need username:password')
#else:
#    user_credentials = args.username[0].split(":")

