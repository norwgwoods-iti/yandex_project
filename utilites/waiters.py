import time

from utilites.check_method import CheckMethod


# from utilites.api import get_file_upload_status

def wait_for_upload_file(api_disk, href, timeout=30):

    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:

        response = api_disk.get_file_upload_status(href)
        response.raise_for_status()

        status = response.json()['status']

        print(f'\nStatus: {status}')

        if status == 'in_progress':
            pass
        if status == 'success':
            return
        if status == 'failed':
            raise AssertionError(
                'Ошибка загрузки файла'
            )

        time.sleep(0.5)

    raise TimeoutError(
        'Загрузка файла не завершена'
    )

