# https://docs.informatica.com/integration-cloud/cloud-api-manager/current-version/api-manager-guide/authentication-and-authorization/oauth-2-0-authentication-and-authorization/python-3-example--invoke-a-managed-api-with-oauth-2-0-authentica.html 
# ^^^ this is the link I pulled the og version of this script from, I've been correcting it and personalizing it.


import sys
import requests
import json
import logging
import time

logging.captureWarnings(True)

test_api_url = "https://api.degreed.com/api/v2/content/courses/"

##
##    function to obtain a new OAuth 2.0 token from the authentication server
##
def get_new_token():

    auth_server_url = "https://api.degreed.com/oauth/token"
    
    print('Enter client id:')
    client_id = str(input())
    
    print('Enter client secret:')
    client_secret = str(input())

    token_req_payload = {'grant_type': 'client_credentials'}

    token_response = requests.post(auth_server_url,
    data=token_req_payload, verify=False, allow_redirects=False,
    auth=(client_id, client_secret))

    if token_response.status_code !=200:
        print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
        sys.exit(1)
    else:
        print("Successfuly obtained a new token")
        tokens = json.loads(token_response.text)
        return tokens['access_token']

## 
## 	obtain a token before calling the API for the first time
## 	the token is valid for 15 minutes
##
token = get_new_token()

while True:
    ##
    ##   call the API with the token
    ##
    api_call_headers = {'Authorization': 'Bearer ' + token}
    api_call_response = requests.get(test_api_url, headers=api_call_headers, verify=False)


    if	api_call_response.status_code == 401:
        token = get_new_token()
    else:
        print(api_call_response.text)

    time.sleep(30)