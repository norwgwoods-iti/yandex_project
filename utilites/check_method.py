
class CheckMethod:

    @staticmethod
    def check_status_code(response, expected_status_code: int):

        if response.status_code == expected_status_code:

            print(f'{response.status_code} - {response.reason}')
            print(f'Успешно! Код ответа совпадает с ожидаемым: {response.status_code}')

        else:
            raise AssertionError(
                f"Ошибка! Ожидался код {expected_status_code}, "
                f"сервер вернул {response.status_code} - ({response.reason}). "
                f"Текст ответа: {response.text[:200]}"
            )


    @staticmethod
    def check_filed_content(response, expected_filed_content: list):

        response_json = response.json()

        assert expected_filed_content in list(response_json), f'Значения полей не совпадают'
        print(f'\nВсе поля присутствуют')
