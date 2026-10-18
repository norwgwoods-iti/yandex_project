import pytest

from tests.test_data.fields_data import FIELD_CONTENT_FILE_METADATA, FIELD_CONTENT_UPLOAD_DIR_OR_FILE, FIELD_DIR_METADATA
from utilites.api import YandexDiskAPI
from utilites.check_method import CheckMethod
from tests.test_data.query_parameters import UPLOAD_FILE_QUERY_PARAMETER, CREATE_DIRECTORY_QUERY_PARAMETER

from utilites.waiters import wait_for_upload_file

class TestYandexDiskAPI:

    @pytest.mark.positive
    @pytest.mark.parametrize(
            'path, href_file', UPLOAD_FILE_QUERY_PARAMETER,
    )
    def test_upload_file_on_disk(self, ya_disk, path:str, href_file: str, create_folder):

        full_path = f'{create_folder}/{path}'

        """ Метод POST """
        post_response = ya_disk.post_upload_file_url(
            path=full_path,
            href_file=href_file
        )
        CheckMethod.check_status_code(response=post_response, expected_status_code=202)
        CheckMethod.check_field(response=post_response, expected_field=FIELD_CONTENT_UPLOAD_DIR_OR_FILE)
        CheckMethod.check_type_field_content(response=post_response, expected_field=FIELD_CONTENT_UPLOAD_DIR_OR_FILE)

        post_response_href = post_response.json()['href']

        wait_for_upload_file(
            ya_disk=ya_disk,
            href=post_response_href
        )

        """ Метод GET """
        get_response = ya_disk.get_directory_or_file_metadata(
            path=full_path
        )
        CheckMethod.check_status_code(response=get_response, expected_status_code=200)
        CheckMethod.check_field(response=get_response, expected_field=FIELD_CONTENT_FILE_METADATA)
        CheckMethod.check_type_field_content(response=get_response, expected_field=FIELD_CONTENT_FILE_METADATA)

        # """ Метод DELETE """
        # delete_response = ya_disk.delete_directory_or_file(
        #     path=path,
        # )
        # CheckMethod.check_status_code(response=delete_response, expected_status_code=204)
    #
    #
    # @pytest.mark.positive
    # @pytest.mark.parametrize(
    #     'path', CREATE_DIRECTORY_QUERY_PARAMETER,
    #
    # )
    # def test_create_directory(self, ya_disk, path: str):
    #
    #     """ Метод PUT """
    #     put_response = ya_disk.put_create_directory(
    #         path=path
    #     )
    #
    #     CheckMethod.check_status_code(response=put_response, expected_status_code=201)
    #     CheckMethod.check_field(response=put_response, expected_field=FIELD_CONTENT_UPLOAD_DIR_OR_FILE)
    #     CheckMethod.check_type_field_content(response=put_response, expected_field=FIELD_CONTENT_UPLOAD_DIR_OR_FILE)
    #
    #     """ Метод GET """
    #     get_response = ya_disk.get_directory_or_file_metadata(
    #         path=path
    #     )
    #
    #     CheckMethod.check_status_code(response=get_response, expected_status_code=200)
    #     CheckMethod.check_field(response=get_response, expected_field=FIELD_DIR_METADATA)
    #     CheckMethod.check_type_field_content(response=get_response, expected_field=FIELD_DIR_METADATA)
    #
    #     """ Метод DELETE """
    #     delete_response = ya_disk.delete_directory_or_file(
    #         path=path,
    #     )
    #     CheckMethod.check_status_code(response=delete_response, expected_status_code=204)



    # @pytest.mark.positive
    # @pytest.mark.parametrize(
    #     'path', CREATE_DIRECTORY_QUERY_PARAMETER,
    # )
    # def test_delete(self,ya_disk, path: str):
    #     """ Метод DELETE """
    #     delete_response = ya_disk.delete_directory_or_file(
    #         path=path,
    #     )
    #
    #
    #
    # @pytest.mark.positive
    # @pytest.mark.parametrize(
    #         'path, href_file', UPLOAD_FILE_QUERY_PARAMETER,
    # )
    # def test_delete_1(self, ya_disk, path:str, href_file: str):
    #     """ Метод DELETE """
    #     delete_response = ya_disk.delete_directory_or_file(
    #         path=path,
    #     )