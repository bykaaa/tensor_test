from pages.search_page import Search
from pages.image_page import Images


def test_yandex_search(browser):
    link = 'https://ya.ru/'
    yandex_page = Search(browser, link)
    yandex_page.open_site()  # 1
    yandex_page.search_field()  # 2
    yandex_page.enter_word("Тензор")  # 3
    yandex_page.suggest_popup()  # 4
    yandex_page.press_enter()  # 5
    yandex_page.search_result()  # 6
    yandex_page.search_to_find()  # 6
    yandex_page.verification_link()  # 7


def test_yandex_image(browser):
    link = 'https://ya.ru/'
    yandex_page = Images(browser, link)
    yandex_page.open_site()  # 1
    yandex_page.open_page()  # 2 - 3
    yandex_page.url_verification()  # 4
    yandex_page.open_category()  # 5
    yandex_page.category_name_search()  # 6
    yandex_page.first_image()  # 7
    yandex_page.open_image()  # 8
    yandex_page.next_button()  # 9
    yandex_page.checking_image_changes()  # 10
    yandex_page.back_button()  # 11 - 12
