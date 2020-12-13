import requests
import json
import jsonpath

from config.config import USERNAME
from config.config import PASSWORD
from config.config import ACCESS_TOKEN
from config.config import TOKEN_ID
from config.config import BASE_URL

# auth related APIs
AUTH_API = '/auth/token/password'
AUDIT_API = '/audit/log'


def get_auth_token(username, password, need_details=False):
    data = {
        "email": username,
        "password": password,
        "timeToLive": "50:00:00"
    }
    headers = {'Content-Type': 'application/json', 'Connection': 'keep-alive'}
    response = requests.post(url=BASE_URL + AUTH_API, data=json.dumps(data), headers=headers)
    if response.status_code == 200:
        response = response.json()
        if need_details:
            return response
        global ACCESS_TOKEN, TOKEN_ID
        TOKEN_ID = response['tokenId']
        ACCESS_TOKEN = response['token']
        print ACCESS_TOKEN
        return ACCESS_TOKEN
    else:
        print 'Unable to authenticate. Please check provided details'
        if need_details:
            return response.status_code, response.reason, json.loads(response.content)
        return response.status_code