__author__ = 'bdm4 and isabeloverman'

import requests
import json 
import subprocess
import sys

authorize_url = "https://staging-app.infosecinstitute.com/portal/api/v1"
token_url = "https://api.byu.edu/token"

#callback url specified when the application was defined
callback_uri = "https://staging-app.infosecinstitute.com/portal/skills/home"

test_api_url = "https://staging-app.infosecisntitute.com/paortal/api/v1/learners?limit=2"

#client (application) credentials - located at apim.byu.edu
client_id = 'clientid123'
client_secret = 'cli3nts3cr3t'

#step A - simulate a request from a browser on the authorize_url - will return an authorization code after the user is
# prompted for credentials.

authorization_redirect_url = authorize_url + '?response_type=code&client_id=' + client_id + '&redirect_uri=' + callback_uri + '&scope=openid'


print ("go to the following url on the browser and enter the code from the returned url: ")
print ("---  " + authorization_redirect_url + "  ---")
authorization_code = input('code: ')

# step I, J - turn the authorization code into a access token, etc
data = {'grant_type': 'authorization_code', 'code': authorization_code, 'redirect_uri': callback_uri}
print ("requesting access token")
access_token_response = requests.post(token_url, data=data, verify=False, allow_redirects=False, auth=(client_id, client_secret))

print ("response")
print (access_token_response.headers)
print ('body: ' + access_token_response.text)

# we can now use the access_token as much as we want to access protected resources.
tokens = json.loads(access_token_response.text)
access_token = tokens['access_token']
print ("access token: " + access_token)

api_call_headers = {'Authorization': 'Bearer ' + access_token}
api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)

print (api_call_response.text)