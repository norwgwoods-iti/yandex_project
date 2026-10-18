
class YandexDiskAPI:
    def __init__(self, base_url: str, http):
        self.base_url = base_url
        self.http = http


    def get_disk_metadata(self):

        resource_url = '/v1/disk'
        url = self.base_url + resource_url

        response = self.http.get(url=url)

        return response


    def get_directory_or_file_metadata(self, path):

        resource_url = '/v1/disk/resources'
        url = self.base_url + resource_url

        query_param = {
            'path': path
        }

        response = self.http.get(
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

        response = self.http.post(
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

        response = self.http.put(
            url=url,
            query_param=query_param
        )

        return response


    def get_file_upload_status(self, href):

        response = self.http.get(url=href)

        return response



    def delete_directory_or_file(self, path):

        resource_url = '/v1/disk/resources'
        url = self.base_url + resource_url

        query_param = {
            'path': path
        }

        response = self.http.delete(
            url=url,
            query_param=query_param
        )

        return response
