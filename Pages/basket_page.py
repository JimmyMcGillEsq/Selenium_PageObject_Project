from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
	
# Проверка, что корзина пуста
	def should_be_empty_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'There is item(s) in the basket'

# Проверка сообщения: "Корзина пуста"
	def should_be_empty_message(self):
		assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), 'There is no empty message'