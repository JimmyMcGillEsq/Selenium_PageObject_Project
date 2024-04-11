from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        log_url = self.browser.current_url
        assert 'login' in log_url, f"Expected 'login' to be in URL, but got {log_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is missing'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is missing'

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.REGISTER_MAIL)
        mail.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS)
        pass1.send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        pass2.send_keys(password)
        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()
