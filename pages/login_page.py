import time
import string
import random
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    GENERATE_LOGIN = "".join([random.choice(string.ascii_letters + string.digits) for i in range(9)])

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "incorrect URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Field login_email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Field login_password is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_EMAIL), "Field registration_email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD), "Field registration_email is not presented"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_REPEAT_PASSWORD), "Field registration_email is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
        print(f"Новый пользователь с Email: {email} зарегистрирован!")
