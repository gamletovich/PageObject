from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest

link = "http://selenium1py.pythonanywhere.com/ "


@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # Page Object initialization,
        # pass the driver instance and url address to the constructor
        page.open()  # open the page
        page.go_to_login_page()  # execute method of the page - redirect to the login page
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
