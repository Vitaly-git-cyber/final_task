from .base_page import BasePage
from .locators import MainPageLocators, LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url , "incorrect URL"
        # реализуйте проверку на корректный url адрес


    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Field login_email is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Field login_password is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Field registration_email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Field registration_email is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD), "Field registration_email is not presented"