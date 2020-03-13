from api.lib.yandex_translate import YandexTranslate as Translate


def test_yandex_translator():

    answer = Translate().get_translate_json_response('ru', "Hello, world!")
    assert answer['lang'] == 'en-ru'
    assert answer['text'] == 'Здравствуй, мир!' or 'Привет, мир!'


def test_another():
    assert 12 == 12
