import requests
import logging

logger = logging.getLogger(__name__)

class CheckMethod:

    @staticmethod
    def method_format_response_in_json(response: requests.Response):

        if isinstance(response, requests.Response):
            response_json = response.json()
        elif isinstance(response, dict):
            response_json = response
        else:
            raise TypeError(
                f'Ожидался requests.Response или dict, а пришел - "{type(response).__name__}"'
            )
        return response_json

    @staticmethod
    def check_status_code(response: requests.Response, expected_status_code):

        assert response.status_code in expected_status_code, (
            f'Ошибка! Ожидался код {expected_status_code}, '
            f'сервер вернул {response.status_code} - ({response.reason}). '
            f'Текст ответа: {response.text[:200]}'
        )

        logger.info(f'%s - %s\nУспешно! Код ответа совпадает с ожидаемым: %s', response.status_code, response.reason, expected_status_code)


    @staticmethod
    def check_field(response: requests.Response, expected_field: dict):
        response_json = CheckMethod.method_format_response_in_json(response)

        def field_path(data, prefix='rt'):
            paths = set()
            for k, v in data.items():
                current_path = f'{prefix}.{k}' if prefix else k # если префикса нет - берем ключ
                paths.add(current_path)

                if isinstance(v, dict):
                    paths |= field_path(v, prefix=current_path)

            return paths

        current_paths = field_path(response_json)
        expected_paths = field_path(expected_field)
        missing_fields = expected_paths - current_paths

        if missing_fields:
            errors = "\n".join(f"- {field}" for field in sorted(missing_fields))

            raise AssertionError(
                f'Ошибка валидации! В ответе обнаружены отсутствующие поля.\n'
                f'Список пропущенных путей:\n'
                f'{errors}'
            )

        logger.info('В ответе присутствуют все ожидаемые поля')


    @staticmethod
    def check_type_field_content(response: requests.Response, expected_field: dict):

        response_json = CheckMethod.method_format_response_in_json(response)

        def field_type(data, expected_structure: dict, prefix='rt'):
            for key, expected_type in expected_structure.items():

                current_path = f'{prefix}.{key}' if prefix else key

                field_value = data[key]

                if isinstance(expected_type, dict):
                    assert isinstance(field_value, dict), (
                        f"Поле '{current_path}' имеет тип {type(field_value).__name__}, "
                        f"но ожидался вложенный объект (dict)"
                    )
                    field_type(data=field_value, expected_structure=expected_type, prefix=current_path)
                else:
                    assert isinstance(field_value, expected_type), (
                        f'Поле "{current_path}" имеет "{type(field_value).__name__}" тип данных, ожидается - '
                        f'"{expected_type.__name__}"'
                    )

        field_type(data=response_json, expected_structure=expected_field, prefix='rt')
        logger.info('Все поля имеют ожидаемый тип данных')


    @staticmethod
    def check_response(response: requests.Response, *, status_code = None, expected_field = None):
        if status_code:
            CheckMethod.check_status_code(response=response, expected_status_code=status_code)
        if expected_field:
            CheckMethod.check_field(response=response, expected_field=expected_field)
            CheckMethod.check_type_field_content(response=response, expected_field=expected_field)
