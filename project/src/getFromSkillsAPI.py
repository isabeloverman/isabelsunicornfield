# author: isabeloverman
# This is a test script. The goal is to get a connection with the Skills API.
# \/ \/ good references \/ \/
# https://www.nylas.com/blog/use-python-requests-module-rest-apis/#how-to-use-python-requests
# https://www.youtube.com/watch?v=W--_EOzdTHk 

# imports
import os
from requests.auth import HTTPBasicAuth
import requests
import json
from pprint import pprint
import csv

# getting API key from user input because I can make that work
print("Enter API key:")
api_token = str(input())     # https://www.geeksforgeeks.org/taking-input-from-console-in-python/

# base URL for API
api_url_base =  "http://app.infosecinstitute.com/portal/api/v1/"

# add on at the end of the url that tell which category on info to bring back
# for Skills courses - courses/
# for Skills learners - learners/
# for Skills learning paths - paths/
endpoint = "paths/"

# headers: I think the authorization here is wrong or something
headers = {'Content-Type': 'application/json', 'Authorization': '{0}'.format(api_token)}

# call API and get response function
def get_course_info():
    
    api_url = '{0}{1}'.format(api_url_base, endpoint)
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
    pprint(course_info, indent=1)  

    # write API response to CSV file
    with open ('courseInfo.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(course_info)
else:
    print('[!] Request Failed')

# pagination
current_page = 1

while current_page != pageCount + 1:
    url = '{0}{1}{2}'.format(api_url_base, endpoint, current_page)
    console.log('getting page ' + current_page)
    response = get_course_info()
    data = json.parse(reponse.getContentText())
    pageCount = data.pageCount
    current_page = pageCount + 1
    