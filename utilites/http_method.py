import requests
import os
from dotenv import load_dotenv
# from utilites.check_method import CheckMethod

load_dotenv()

class HttpMethod:
    token = os.environ['OAUTH_TOKEN']

    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }

    cookies = {}

    @staticmethod
    def get(url, query_param: dict | None = None):

        response = requests.get(url=url, params=query_param, headers=HttpMethod.headers, cookies=HttpMethod.cookies, timeout=(5, 30))

        return response


    @staticmethod
    def post(url, body: dict | None = None, query_param: dict | None = None):

        response = requests.post(url=url, params=query_param, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookies)

        return response


    @staticmethod
    def put(url, query_param: dict | None = None):

        response = requests.put(url=url, params=query_param, headers=HttpMethod.headers, cookies=HttpMethod.cookies)

        return response


    @staticmethod
    def delete(url, query_param: dict | None = None, body: dict | None = None):

        response = requests.delete(url=url, params=query_param, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookies, timeout=(5, 30))

        return response

