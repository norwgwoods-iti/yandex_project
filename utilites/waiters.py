import time
import logging

logger = logging.getLogger(__name__)

def wait_for_upload_file(ya_disk, href, timeout=30):

    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:

        response = ya_disk.get_file_upload_status(href)
        response.raise_for_status()

        status = response.json()['status']

        logger.info(f'Status: {status}')

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

