import time
import pytest

from final_task.pages.basket_page import BasketPage
from final_task.pages.login_page import LoginPage
from final_task.pages.product_page import ProductPage


@pytest.mark.skip("Временно не работающий тест")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Тест проверяет, что гость не должен видеть сообщение об успешном добавлении продукта в корзину.
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()
    time.sleep(10)


@pytest.mark.skip("Временно не работающий тест")
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Тест проверяет, что нет сообщения об успешном добавлении продукта в корзину.
    """
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    """
    Тест проверяет, что гость видит ссылку страницу логина со страницы продукта.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Тест проверяет, что гость может перейти на страницу логина со страницы продукта.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Тест проверяет, что гость при открытии корзины со страницы продукта видит, что корзина пуста и присутствует
     соответствующая надпись.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_basket_empty()
    page.is_basket_label_empty()

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    """
    Тест проверяет, что гость может добавить товар в корзину. Проверяется, что имя продукта соответствует
    имени продукта в корзине и цена продукта соответствует цене в корзине.
    """
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.check_name_product_in_basket()
    page.check_price_product_in_basket()


def test_guest_cant_see_success_message(browser):
    """Тест проверяет, что гость не видит сообщение о добавлении товара в корзину."""
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        """
        Подготовка к тестам. Происходит регистрация нового пользователя и проверка, что пользователь зарегистрирован.
        """
        email = str(time.time()) + "@fakemail.org"
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, LoginPage.GENERATE_LOGIN)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """Тест проверяет, что пользователь не видит сообщение о добавлении товара в корзину."""
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        Тест проверяет, что пользователь может добавить товар в корзину. Проверяется, что имя продукта соответствует
        имени продукта в корзине и цена продукта соответствует цене в корзине.
        """
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.check_name_product_in_basket()
        page.check_price_product_in_basket()
