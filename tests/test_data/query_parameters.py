import pytest

UPLOAD_FILE_QUERY_PARAMETER = [
    pytest.param(
       'Fudji',
       'https://avatars.mds.yandex.net/get-altay/15081387/2a000001959b3e16597323478c3ff0612ee3/orig',
       id='Fudji_image_upload'
    ),
    pytest.param(
       'Car',
       'https://img.goodfon.ru/wallpaper/nbig/0/4e/badfon-bmw-m3-kabriolet-belyy-mashina-896.webp',
       id='Car_image_upload'
    ),
    pytest.param(
       'House',
       'https://www.rift.ru/wp-content/uploads/2026/03/photo_10_2026-03-26_15-02-57.jpg',
       id='House_image_upload'
    ),
]

CREATE_DIRECTORY_QUERY_PARAMETER = [
    pytest.param(
        'Music',
        id='Music_directory_create'
    ),
    pytest.param(
        'Image',
        id='Image_directory_create'
    ),
    pytest.param(
        'Document',
        id='Document_directory_create'
    ),
]
