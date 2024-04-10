from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")

class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ITEM_NAME = (By.CSS_SELECTOR, 'div h1')
    ITEM_PRICE = (By.CSS_SELECTOR, 'div.product_main p.price_color')
    CART_ITEM_NAME =(By.CSS_SELECTOR, '#messages div.alert:first-child strong') 
    CART_ITEM_PRICE = (By.CSS_SELECTOR, 'div.alert p strong')
