from urllib import request

import requests

from utilites.http_method import HttpMethod

class YandexDiskAPI:

    base_url = 'https://cloud-api.yandex.net'

    def get_disk_metadata(self):

        resource_url = '/v1/disk'
        url = self.base_url + resource_url

        response = HttpMethod.get(url=url)
        return response


    def get_directory_or_file_metadata(self, path):

        resource_url = '/v1/disk/resources'
        url = self.base_url + resource_url

        query_param = {
            'path': path
        }

        response = HttpMethod.get(
            url=url,
            query_param=query_param
        )

        return response


    def post_upload_file_url(self, path, href_file):

        resource_url = '/v1/disk/resources/upload'
        url = self.base_url + resource_url

        query_param = {
            'path': path,
            'url': href_file
        }

        response = HttpMethod.post(
            url=url,
            query_param=query_param
        )
        return response


    def put_create_directory(self, path):

        resource_url = '/v1/disk/resources'
        url = self.base_url + resource_url

        query_param = {
            'path': path
        }

        response = HttpMethod.put(
            url=url,
            query_param=query_param
        )
        return response


    @staticmethod
    def get_file_upload_status(href):

        response = HttpMethod.get(url=href)

        return response



    def delete_directory_or_file(self, path):

        resource_url = '/v1/disk/resources'
        url = self.base_url + resource_url

        query_param = {
            'path': path
        }

        response = HttpMethod.delete(
            url=url,
            query_param=query_param
        )
        return response
