from .base_page import BasePage
from .locators import LoginPageLocators
import faker
import time
from selenium.webdriver.common.keys import Keys


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find("accounts/login/"), "Wrong URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email=faker.Faker().email(), password=faker.Faker().password()):
        assert self.is_element_present(*LoginPageLocators.EMAIL_FOR_REGISTRATIOM), \
            "E-mail field is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD_FOR_REGISTRATION), \
            "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.CONFIRM_PASSWORD_FOR_REGISTRATION), \
            "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), \
            "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), \
            "Login form is not presented"

        email_element = self.browser.find_element(*LoginPageLocators.EMAIL_FOR_REGISTRATIOM)
        password_element = self.browser.find_element(*LoginPageLocators.PASSWORD_FOR_REGISTRATION)
        confirm_password_element = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FOR_REGISTRATION)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)

        email_element.send_keys(email)
        password_element.send_keys(password)
        confirm_password_element.send_keys(password)
        register_button.click()

        if self.is_element_present(*LoginPageLocators.EMAIL_ERROR):
            self.register_new_user("A")  # adding in the en
