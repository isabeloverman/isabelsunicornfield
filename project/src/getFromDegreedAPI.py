# author: isabeloverman
# This is a test script. The goal is to get a connection with the Degreed API.
# \/ \/ good references \/ \/
# https://www.nylas.com/blog/use-python-requests-module-rest-apis/#how-to-use-python-requests
# https://www.youtube.com/watch?v=W--_EOzdTHk 
# https://www.digitalocean.com/community/tutorials/how-to-use-web-apis-in-python-3 
# https://docs.informatica.com/integration-cloud/cloud-api-manager/current-version/api-manager-guide/authentication-and-authorization/oauth-2-0-authentication-and-authorization/python-3-example--invoke-a-managed-api-with-oauth-2-0-authentica.html



# imports
import os
from requests.auth import HTTPBasicAuth
import requests
import argparse
import json
from pprint import pprint
import sys


# getting API key from user input because I can make that work
print("Enter API key:")
api_token = str(input())     # https://www.geeksforgeeks.org/taking-input-from-console-in-python/

# base URL for API
api_url_base =  "https://api.betatest.degreed.com/api/v2/"

# add on at the end of the url that tell which category on info to bring back
# for Degreed courses - content/courses/
# for Degreed users - users/
# for Degreed required learning = required-learning/ - gets a 403
# for Degreed completions - completions/ - gets a 403
information_category = "content/courses/"

# headers: I think the authorization here is wrong or something
headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + api_token}

# call API and get response function
def get_course_info():
    
    api_url = '{0}{1}'.format(api_url_base, information_category)
    print(api_url)
    response = requests.get(api_url, headers=headers)
    print(headers)
    
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
    pprint(course_info, indent=1)  
else:
    print('[!] Request Failed')


