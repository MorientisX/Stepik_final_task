from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():

    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTATION_PASSWORD_REPEAT = (By.CSS_SELECTOR, "id_registration-password2")

    LOGIN_URL = (By.CSS_SELECTOR, "login-redirect_url")


    
