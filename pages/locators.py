from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID,"id_login-password")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_REPEAT_PASSWORD = (By.ID, "id_registration-password2")

class ProductPageLocators:
    ADD_BASKET = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    PRODUCT_NAME = (By.XPATH, "//div/h1")
    PRODUCT_PRICE = (By.XPATH, "//div[contains(@class,'product_main')]/p[@class='price_color']")
    BASKET_NAME = (By.XPATH, "(//div[@class='alertinner '])[1]/strong")
    BASKET_PRICE_ONE = (By.XPATH, "(//div[@class='alertinner '])[3]/p/strong")
    BASKET_PRICE_NAVBAR = (By.XPATH, "//div[contains(@class,'basket-mini')]")
