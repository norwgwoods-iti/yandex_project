import pytest
import requests
import os
from dotenv import load_dotenv
import uuid

from utilites.api import YandexDiskAPI
from utilites.check_method import CheckMethod
from utilites.http_method import HttpMethod

load_dotenv()

BASE_URL = 'https://cloud-api.yandex.net'
token = os.environ['OAUTH_TOKEN']


@pytest.fixture(scope='session')
def base_url():
    return BASE_URL

@pytest.fixture(scope='session')
def api_session():
    session = requests.Session()
    session.headers.update({
        'Content-Type': 'application/json',
        'Authorization': token
    })

    yield session

    session.close()


@pytest.fixture(scope='session')
def http(api_session):
    return HttpMethod(session=api_session)


@pytest.fixture(scope='session')
def ya_disk(base_url, http):
    return YandexDiskAPI(base_url=base_url, http=http)


@pytest.fixture
def create_folder(ya_disk):
    path = f'/autotest_{uuid.uuid4().hex[:8]}'

    put_response = ya_disk.put_create_directory(path=path)
    CheckMethod.check_response(response=put_response, status_code=201)

    yield path

    delete_response = ya_disk.delete_directory_or_file(path=path)
    assert delete_response.status_code in (204, 202), delete_response.text