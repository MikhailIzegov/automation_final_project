from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Seems like it's NOT login page: check URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email is not displayed"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Password field for logging in is " \
                                                                           "not displayed"
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_BUTTON), "FORGOT_PASSWORD_BUTTON is not " \
                                                                                   "displayed"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "LOGIN_BUTTON is not displayed"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_EMAIL), "Sign up email is not displayed"
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_PASSWORD), "Sign up password is not displayed"
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_PASSWORD_REPETITION), "Sign up password2 is not " \
                                                                                        "displayed"
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_BUTTON), "SIGN_BUTTON is not displayed"
