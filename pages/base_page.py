from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_site(self):
        """Метод открывает браузер"""
        return self.browser.get(self.url)

    def find_element(self, locator):
        """Находит по заданному локатору элемент на странице и возвращает его."""
        return Wait(self.browser, 10).until(EC.presence_of_element_located(locator))

    def get_current_image_src(self, locator):
        """Метод возвращает в виде строки ссылку на текущее открытое изображение в модальном окне на странице
            с картинками"""
        return self.find_element(locator).get_attribute("src")
