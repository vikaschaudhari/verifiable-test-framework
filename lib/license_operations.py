import requests
import json
import jsonpath

from config import config
from lib import auth_operations

GET_LICENSE_TYPE_API = '/licensetypes'


def get_provider_id_list(provider_name, license_state, license_number=None):
    """
    This function will return provider id list based
    on provider name and license state
    """
    GET_PROVIDERS_API = '/providers?count=100'
    if config.ACCESS_TOKEN == '':
        token = auth_operations.get_auth_token(config.USERNAME, config.PASSWORD)
    else:
        token = config.ACCESS_TOKEN
    headers = {'Content-Type': 'application/json',
               'Connection': 'keep-alive',
               'Authorization': 'Bearer %s' % token}
    provider_id_list = []
    response = requests.get(url=config.BASE_URL + GET_PROVIDERS_API, headers=headers)
    if response.status_code == 200:
        response = response.json()
        if license_number:
            # jsonpath_expr = '$..[?(@.licenseNumber=="{0}")]..providerId'.format(license_number)
            jsonpath_expr = '$..[?(@.licenseNumber=="{0}")]'.format(license_number)
            print jsonpath_expr
            provider_id_list = jsonpath.jsonpath(response, jsonpath_expr)
        else:
            first_name, last_name = provider_name.split(' ')
            for each_item in response["items"]:
                if each_item["firstName"] == first_name and each_item["lastName"] == last_name:
                    for each_license in each_item["licenses"]:
                        if each_license["licenseType"]["source"]["state"] == license_state:
                            provider_id_list.append(each_license["providerId"])
        return provider_id_list
    else:
        print 'something went wrong'
        return response.status_code


# def get_specific_license_details(provider_id, license_number):
#     """
#     This function returns license details based on
#     provider ID and license number
#     """
#     GET_SPECIFIC_LICENSE_API = '/providers/{0}/licenses/{1}'.format(provider_id, license_number)
#     headers = {'Content-Type': 'application/json',
#                'Connection': 'keep-alive',
#                'Authorization': 'Bearer %s' % ACCESS_TOKEN}
#     response = requests.get(config.BASE_URL+GET_SPECIFIC_LICENSE_API, headers=headers)
#     if response.status_code == 200:
#         response = response.json()
#         pass
#     else:
#         print 'something went wrong'
#         return response.status_code
#