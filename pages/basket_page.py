from .base_page import BasePage
from .locators import BasePageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert not self.is_element_present(*BasketPageLocators.BASKET_PRODUCTS), "basket products is not presented"

    def should_not_be_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_PRODUCTS), "basket products is not presented"

    def is_basket_label_empty(self):
        assert "Your basket is empty." in  self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_LABEL).text


    def should_not_be_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY_LABEL), \
            "Корзина не пуста"

    def should_not_be_success_message_disappeared(self):
        assert self.is_disappeared(*BasketPageLocators.BASKET_EMPTY_LABEL), \
            "Корзина не пуста"