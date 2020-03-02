from api.lib.yandex_translate import YandexTranslate as Translate
import allure-pytest

def test_yandex_translator():

    answer = Translate().get_translate('ru', "Hello, world!")
    assert answer['lang'] == 'en-ru'
    assert answer['text'] == 'Здравствуй, мир!' or 'Привет, мир!'