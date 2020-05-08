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


class ProductPageLocators():

    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form>.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (By.CSS_SELECTOR, "div.alertinner ")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

    
