from selenium.common import NoSuchElementException
from pages.base_page import BasePage
from loccators.search_locators import SearchLocators
from selenium.webdriver.common.keys import Keys


class Search(BasePage):

    def search_field(self):
        """Проверка наличия поля поиска"""
        assert self.find_element(SearchLocators.SEARCH_FIELD), 'Строка поиска не найдена'

    def enter_word(self, word):
        """Ввод запроса"""
        search_panel = self.find_element(SearchLocators.SEARCH_FIELD)
        search_panel.click()
        search_panel.send_keys(word)

    def suggest_popup(self):
        """Проверка появления попапа с подсказкой"""
        assert self.find_element(SearchLocators.POPUP), 'Попап с подсказками не появляется'

    def press_enter(self):
        """Жмем Enter"""
        press_key = self.find_element(SearchLocators.SEARCH_FIELD)
        press_key.send_keys(Keys.ENTER)

    def search_result(self):
        """Проверка наличия результатов поиска"""
        assert self.find_element(SearchLocators.SEARCH_RESULT_PAGE)

    def search_to_find(self):
        """Метод проверяющий, что появилась страница результатов поиска"""
        assert self.find_element(SearchLocators.FIND_SEARCH)

    def verification_link(self):
        """Метод проверяющий, что 1 ссылка ведет на сайт tensor.ru"""

        try:
            self.browser.find_element(*SearchLocators.LINK_ONE).text == 'tensor.ru'
        except NoSuchElementException:
            return False
        return True
