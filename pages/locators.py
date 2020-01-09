from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form button")
    ITEM_NAME = (By.CSS_SELECTOR, "#content_inner h1")
    ADDED_ITEM_NAME = (By.CSS_SELECTOR, "#messages strong") #ADDED_ITEM_NAME[0]
    ITEM_PRICE = (By.CSS_SELECTOR, "#content_inner p")
    ADDED_ITEM_PRICE = (By.CSS_SELECTOR, "#messages strong") #ADDED_ITEM_PRICE[3]