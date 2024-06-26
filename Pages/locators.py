from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, 'div.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTER_MAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_PASS = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTER_PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BTN = (By.CSS_SELECTOR, '#register_form button')

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')

class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, 'div h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    CART_ITEM_NAME =(By.CSS_SELECTOR, '#messages div.alert:first-child strong') 
    CART_ITEM_PRICE = (By.CSS_SELECTOR, 'div.alert p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert:first-child')

