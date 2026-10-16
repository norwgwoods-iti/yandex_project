import time

import pytest

from utilites.api import YandexDiskAPI
from utilites.check_method import CheckMethod
from tests.test_data.query_parameter import UPLOAD_FILE_QUERY_PARAMETER

class TestYandexDiskAPI:

    api_disk = YandexDiskAPI()

    @pytest.mark.parametrize(
        'path, href_file', UPLOAD_FILE_QUERY_PARAMETER,
    )
    def test_upload_file_on_disk(self, path:str, href_file: str):

        response = self.api_disk.post_upload_file_url(
            path=path,
            href_file=href_file
        )


        # CheckMethod.check_status_code(response=response, expected_status_code=202)



    @pytest.mark.parametrize(
        'path, href_file', UPLOAD_FILE_QUERY_PARAMETER,
    )
    def test_get_file_metadata(self, path: str, href_file: str):

        time.sleep(5)

        response = self.api_disk.get_directory_or_file_metadata(
            path=path
        )

        print(response.json())


        # CheckMethod.check_status_code(response=response, expected_status_code=200)

    #     # CheckMethod.check_filed_content(response=response, expected_filed_content=["path", "type", "name"])
    #     # print(response.json())



    @pytest.mark.parametrize(
        'path, href_file', UPLOAD_FILE_QUERY_PARAMETER,
    )
    def test_delete_file_on_disk(self, path: str, href_file: str):

        response = self.api_disk.delete_directory_or_file(
            path=path,
        )
    #
    #
    #
    #     CheckMethod.check_status_code(response=response, expected_status_code=204)


