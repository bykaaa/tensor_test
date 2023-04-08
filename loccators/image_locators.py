from selenium.webdriver.common.by import By


class ImageLocators:
    SEARCH_FIELD = (By.ID, 'text')
    POPUP = (By.CSS_SELECTOR, 'div.mini-suggest__popup.mini-suggest__popup_svg_yes')
    MENU = (By.XPATH, "//a[@class='home-link2 services-suggest__item services-suggest__item-more home-link2_color_black home-link2_hover_secondary']")
    IMAGE = (By.XPATH, '//a[@aria-label="Картинки"]')
    FIRST_IMAGE_CATEGORY = (By.CSS_SELECTOR, '.PopularRequestList-Item.PopularRequestList-Item_pos_0')
    FIRST_IMAGE_CATEGORY_NAME = (By.XPATH, '//*[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]/a/div[2]')
    SEARCH_IMAGE_FIELD = (By.CLASS_NAME, 'mini-suggest__input')
    FIRST_IMAGE = (By.CLASS_NAME, 'serp-item_pos_0')
    MMIMAGE = (By.CLASS_NAME, 'MMImage-Origin')
    IMAGE_NEXT = (By.CSS_SELECTOR, '.CircleButton_type_next')
    IMAGE_BACK = (By.CSS_SELECTOR, '.CircleButton_type_prev')
