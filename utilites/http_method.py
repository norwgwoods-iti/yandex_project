import requests
# import os
# from dotenv import load_dotenv
import logging
# from utilites.check_method import CheckMethod

logger = logging.getLogger(__name__)
# load_dotenv()

class HttpMethod:

    def __init__(self, session: requests.Session | None = None):
        self.session = session or requests.Session()

    """ Метод GET """
    def get(self, url, query_param: dict | None = None):
        logger.info('\n---> GET %s', url)

        response = self.session.get(
            url=url,
            params=query_param,
            timeout=(5, 30)
        )

        logger.info(f'<--- STATUS %s [%.0fms]', response.status_code, response.elapsed.total_seconds() * 1000)
        if query_param:
            logger.info(f'<--- QUERY %s', query_param)

        return response


    def post(self, url, json: dict | None = None, query_param: dict | None = None):
        logger.info('\n---> POST %s', url)

        response = self.session.post(
            url=url,
            params=query_param,
            json=json,
            timeout=(5, 30)
        )

        logger.info(f'<--- STATUS %s [%.0fms]', response.status_code, response.elapsed.total_seconds() * 1000)
        if query_param:
            logger.info(f'<--- QUERY %s', query_param)

        return response


    def put(self, url, json:dict | None = None, query_param: dict | None = None):
        logger.info('\n---> PUT %s', url)

        response = self.session.put(url=url,
            json=json,
            params=query_param,
            timeout=(5, 30)
        )

        logger.info(f'<--- STATUS %s [%.0fms]', response.status_code, response.elapsed.total_seconds() * 1000)
        if query_param:
            logger.info(f'<--- QUERY %s', query_param)

        return response


    def delete(self, url, query_param: dict | None = None, body: dict | None = None):
        logger.info('\n---> DELETE %s', url)

        response = self.session.delete(
            url=url,
            params=query_param,
            json=body,
            timeout=(5, 30)
        )

        logger.info(f'<--- STATUS %s [%.0fms]', response.status_code, response.elapsed.total_seconds() * 1000)
        if query_param:
            logger.info(f'<--- QUERY %s', query_param)

        return response

