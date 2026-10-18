import requests
import os
from dotenv import load_dotenv
import logging
# from utilites.check_method import CheckMethod

logger = logging.getLogger(__name__)
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
        logger.info('\n---> GET %s', url)

        response = requests.get(url=url, params=query_param, headers=HttpMethod.headers, cookies=HttpMethod.cookies, timeout=(5, 30))

        logger.info(f'<--- STATUS %s [%.0fms]', response.status_code, response.elapsed.total_seconds() * 1000)
        if query_param:
            logger.info(f'<--- QUERY %s', query_param)

        return response


    @staticmethod
    def post(url, body: dict | None = None, query_param: dict | None = None):
        logger.info('\n---> POST %s', url)

        response = requests.post(url=url, params=query_param, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookies)

        logger.info(f'<--- STATUS %s [%.0fms]', response.status_code, response.elapsed.total_seconds() * 1000)
        if query_param:
            logger.info(f'<--- QUERY %s', query_param)

        return response


    @staticmethod
    def put(url, query_param: dict | None = None):
        logger.info('\n---> PUT %s', url)

        response = requests.put(url=url, params=query_param, headers=HttpMethod.headers, cookies=HttpMethod.cookies)

        logger.info(f'<--- STATUS %s [%.0fms]', response.status_code, response.elapsed.total_seconds() * 1000)
        if query_param:
            logger.info(f'<--- QUERY %s', query_param)

        return response


    @staticmethod
    def delete(url, query_param: dict | None = None, body: dict | None = None):
        logger.info('\n---> DELETE %s', url)

        response = requests.delete(url=url, params=query_param, json=body, headers=HttpMethod.headers, cookies=HttpMethod.cookies, timeout=(5, 30))

        logger.info(f'<--- STATUS %s [%.0fms]', response.status_code, response.elapsed.total_seconds() * 1000)
        if query_param:
            logger.info(f'<--- QUERY %s', query_param)

        return response

