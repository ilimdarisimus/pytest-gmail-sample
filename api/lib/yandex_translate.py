import requests


class YandexTranslate:
    """Класс методов взаимодействия с API Яндекс Переводчика"""

    def __init__(self, api_key='trnsl.1.1.20200227T073147Z.74788de9ada56ae1.c1ac481afc71ba658f39c0c6809f12deb2d01a75',
                 host='translate.yandex.net'):
        self.api_key = api_key
        self.host = host

    def get_translate_json_response(self, lang, text):
        url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
        headers = {'Host': self.host,
                   'Accept': 'application/json',
                   'Content-Type': 'application/x-www-form-urlencoded'
                   }

        data = f'key={self.api_key}&lang={lang}&text={text}'
        answer = requests.post(url, data=data, headers=headers).json()
        return answer

    def