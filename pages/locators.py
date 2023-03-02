from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "[name='login-username']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "[name='login-password']")
    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[text()="Я забыл пароль"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")
    SIGN_UP_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    SIGN_UP_PASSWORD = (By.CSS_SELECTOR, "[name='registration-password1']")
    SIGN_UP_PASSWORD_REPETITION = (By.CSS_SELECTOR, "[name='registration-password2']")
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
