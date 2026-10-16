from utilites.http_method import HttpMethod

class YandexDiskAPI:

    base_url = 'https://cloud-api.yandex.net'

    def get_disk_metadata(self):

        resource_url = '/v1/disk'

        url = self.base_url + resource_url

        response = HttpMethod.get(url=url)

        response_json = response.json()

        return response_json



    def get_directory_or_file_metadata(self, path):

        resource_url = '/v1/disk/resources'

        url = self.base_url + resource_url

        # query_param = {
        #     'path': 'Image'
        # }
        #
        query_param = {
            'path': path
        }

        response = HttpMethod.get(url=url, query_param=query_param)

        # response_json = response.json()

        return response


    def post_upload_file_url(self, path, href_file):

        resource_url = '/v1/disk/resources/upload'

        url = self.base_url + resource_url

        # query_param = {
        #     'path': 'Image',
        #     'url': 'https://avatars.mds.yandex.net/get-altay/15081387/2a000001959b3e16597323478c3ff0612ee3/orig'
        # }
        query_param = {
            'path': path,
            'url': href_file
        }

        response = HttpMethod.post(url=url, query_param=query_param)

        # response_json = response.json()

        return response


    def put_create_directory(self, path):

        resource_url = '/v1/disk/resources'

        url = self.base_url + resource_url

        # param = {
        #     'path': 'Image'
        # }

        query_param = {
            'path': path
        }

        response = HttpMethod.put(url=url, query_param=query_param)

        response_json = response.json()

        return response_json


    def get_meta_file(self):

        resource_url = '/v1/disk/operations/c3b692a9ec8c0baa1d17f902d76f82123ee9a23e03749de0c328c22a2b90ec2f'

        url = self.base_url + resource_url

        response = HttpMethod.get(url=url)

        response_json = response.json()

        return response_json



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

#
# if __name__ == '__main__':
#     kak = YandexDiskAPI()
#     # print(kak.get_meta())
#     # print('_______________________________________')
#     # print(kak.put_create_directory())
#     # print(kak.post_file())
#     # print(kak.get_meta_directory())
#
#     # print(kak.post_file())
#
#     print(kak.get_meta_file())
#
#
#     'disk%3A%2FMusic'
