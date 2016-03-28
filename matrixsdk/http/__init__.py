# -*- coding: utf-8 -*-

'''
© 2016 I-Value Tecnologia
Authored by: Armando Miani
Licensed under CDDL 1.0
'''

import requests

def execute_get(endpoint, params={}):    
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(endpoint, headers=headers, params=params)
    return __envelope_response(response)


def __envelope_response(response):
    return {
        'body': response.json(),
        'status_code': response.status_code
    }