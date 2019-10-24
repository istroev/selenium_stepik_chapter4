from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.is_valid_url(LoginPageLocators.LOGIN_URL), "Login form is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        register_name = self.browser.find_element(*LoginPageLocators.REGISTER_NAME)
        register_name.send_keys(email)
        register_pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        register_pass1.send_keys(password)
        register_pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        register_pass2.send_keys(password)
        register_submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        register_submit.click()
