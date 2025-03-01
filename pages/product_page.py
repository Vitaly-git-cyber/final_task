from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        basket_link.click()
        BasePage.solve_quiz_and_get_code(self)

    def should_be_add_basket_link(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), "basket link is not presented"

    def check_name_product_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.BASKET_NAME).text, "product name in basket incorrect"
        print("Товар добавлен в корзину")

    def check_price_product_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE_ONE).text, "price product in basket - incorrect"
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element(
            *ProductPageLocators.BASKET_PRICE_NAVBAR).text, "price product in navbar - incorrect"
        print(f'Общая стоимость корзины: {self.browser.find_element(*ProductPageLocators.BASKET_PRICE_NAVBAR).text.split(":")[1]}')
