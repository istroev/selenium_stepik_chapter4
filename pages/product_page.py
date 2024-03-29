from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        add_button.click()

    def check_added_item(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        basket_name = self.browser.find_element(*ProductPageLocators.ADDED_ALERT).text
        assert item_name == basket_name, "Basket item name {} not equal to item name {} on page {}".format(basket_name, item_name, self.url)

    def check_basket_price(self):
        price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_ALERT).text
        assert price == basket_price, "Basket price {} is not equal to item {} price on page {}".format(basket_price, price, self.url)

    def check_success_message_not_present(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_ALERT)

    def check_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_ALERT)
