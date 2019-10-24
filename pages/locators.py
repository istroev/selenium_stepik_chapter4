from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, 'span > a[href*="basket"]')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class LoginPageLocators():
    LOGIN_URL = '/accounts/login/'
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    LOGIN_NAME = (By.CSS_SELECTOR, '#id_login-username')
    LOGIN_PASS = (By.CSS_SELECTOR, '#id_login-password')
    LOGIN_SUBMIT = (By.CSS_SELECTOR, '[name="login_submit"]')
    REGISTER_NAME = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators():
    ITEM_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    ADD_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ADDED_ALERT = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    PRICE_ALERT = (By.CSS_SELECTOR, '#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong')


class BasketPageLocators():
    BASKET_URL = '/basket/'
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner > p')
