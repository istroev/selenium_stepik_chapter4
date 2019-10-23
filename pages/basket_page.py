from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_not_present_elements()
        self.should_have_empty_basket_message()

    def should_be_basket_url(self):
        assert self.is_valid_url(BasketPageLocators.BASKET_URL), "Basket page is not presented"

    def should_be_not_present_elements(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket page has elements"

    def should_have_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), "Basket page empty message not present"
