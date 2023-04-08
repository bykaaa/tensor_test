from selenium.common import NoSuchElementException
from loccators.image_locators import ImageLocators
from pages.base_page import BasePage


class Images(BasePage):

    image = str
    old_image = str

    def open_page(self):
        """Метод открывает страницу 'картинки' в яндекса (больше нет кнопки меню)"""
        search_panel = self.find_element(ImageLocators.SEARCH_FIELD)
        search_panel.click()
        menu_button = self.find_element(ImageLocators.MENU)
        menu_button.click()
        image_button = self.find_element(ImageLocators.IMAGE)
        image_button.click()

    def url_verification(self):
        """Метод для проверки url"""
        url = self.browser.current_url
        try:
            url == 'https://yandex.ru/images/'
        except NoSuchElementException:
            return False
        window_after = self.browser.window_handles[1]
        self.browser.switch_to.window(window_after)
        return True

    def open_category(self):
        """Метод для открытия первой категории"""
        first_category = self.find_element(ImageLocators.FIRST_IMAGE_CATEGORY)
        first_category.click()

    def category_name_search(self):
        """Проверяет, что название категории отображается в поле поиска"""
        first_image_category_name = self.find_element(ImageLocators.FIRST_IMAGE_CATEGORY_NAME).text
        search_field_suggest_text = self.find_element(ImageLocators.SEARCH_IMAGE_FIELD).get_attribute("value")
        assert first_image_category_name == search_field_suggest_text

    def first_image(self):
        """Открытие первой картинки"""
        img = self.find_element(ImageLocators.FIRST_IMAGE)
        img.click()

    def open_image(self):
        """Проверяет, что картинка открылась"""
        self.image = self.get_current_image_src(ImageLocators.MMIMAGE)
        assert self.find_element(ImageLocators.MMIMAGE)

    def next_button(self):
        """Метод нажатия кнопки вперед"""
        self.old_image = self.get_current_image_src(ImageLocators.MMIMAGE)
        self.find_element(ImageLocators.IMAGE_NEXT).click()

    def checking_image_changes(self):
        """Метод проверяет, что картинка сменилась"""
        image = self.get_current_image_src(ImageLocators.MMIMAGE)
        assert image != self.old_image

    def back_button(self):
        """Метод нажимает кнопку назад и проверяет, что картинка осталась из шага 8"""
        self.find_element(ImageLocators.IMAGE_BACK).click()
        image1 = self.get_current_image_src(ImageLocators.MMIMAGE)
        assert self.image == image1
