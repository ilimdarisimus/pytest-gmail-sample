from ui.pages.YandexPages import SearchHelper
import pytest


class TestYandex:

    def test_header_elements(self, browser):
        yandex_main_page = SearchHelper(browser)
        yandex_main_page.go_to_site()
        yandex_main_page.enter_word("Hello")
        yandex_main_page.click_on_the_search_button()
        elements = yandex_main_page.check_navigation_bar()
        assert "Картинки" and "Видео" in elements

    def test_search(self, browser):
        yandex_main_page = SearchHelper(browser)
        yandex_main_page.go_to_site()
        yandex_main_page.enter_word("Hello World")
