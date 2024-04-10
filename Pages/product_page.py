from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):

	def click_add_to_cart_btn(self):
	    add_to_cart_btn =  self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BTN)
	    add_to_cart_btn.click()

	def should_be_right_name_in_cart(self):
		item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
		cart_item_name = self.browser.find_element(*ProductPageLocators.CART_ITEM_NAME)
		assert item_name.text == cart_item_name.text, f'Book name in cart: {cart_item_name} doesnt match real book name: {item_name}'

	def should_be_right_price(self):
		item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
		cart_item_price = self.browser.find_element(*ProductPageLocators.CART_ITEM_PRICE)
		assert item_price.text == cart_item_price.text, f'Book price in cart: {cart_item_price} doesnt match real book price: {item_price}'