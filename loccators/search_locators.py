from selenium.webdriver.common.by import By


class SearchLocators:
    SEARCH_FIELD = (By.ID, 'text')
    POPUP = (By.CSS_SELECTOR, 'div.mini-suggest__popup.mini-suggest__popup_svg_yes')
    SEARCH_RESULT = (By.XPATH, '//div[@class="content__left"]/li')
    SEARCH_RESULT_PAGE = (By.ID, 'search-result')
    FIND_SEARCH = (By.XPATH, "//*[contains(@class, 'serp-list serp-list_left_yes')]")
    LINK_ONE = (By.XPATH, '//*[@id="search-result"]/li[1]')
