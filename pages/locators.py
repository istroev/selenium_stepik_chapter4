from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    LOGIN_URL = '/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators():
    ITEM_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDED_ALERT = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRICE_ALERT = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')
