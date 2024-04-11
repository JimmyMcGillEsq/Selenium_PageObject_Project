from .Pages.product_page import ProductPage
from .Pages.login_page import LoginPage
from .Pages.basket_page import BasketPage
import pytest
import time

# Ввел параметризацию - 10 тестовых страниц, одну пометил как ожидаемо падающую(XFail)
@pytest.mark.skip
@pytest.mark.parametrize('promo', ['?promo=offer0', '?promo=offer1','?promo=offer2','?promo=offer3',
	'?promo=offer4','?promo=offer5','?promo=offer6',
	pytest.param('?promo=offer7', marks=pytest.mark.xfail(reason='Expected bug, wont be fixed')),'?promo=offer8','?promo=offer9'])
def test_guest_can_add_product_to_basket(browser, promo):
	link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
	page = ProductPage(browser, link)
	page.open()
	page.click_add_to_cart_btn()
	page.solve_quiz_and_get_code()
	page.should_be_right_name_in_cart()
	page.should_be_right_price()

@pytest.mark.skip
def test_should_be_right_name_in_cart(browser):
	page = ProductPage(browser, link)
	page.open()
	page.click_add_to_cart_btn()
	page.solve_quiz_and_get_code()
	page.should_be_right_name_in_cart()

@pytest.mark.skip
def test_should_be_right_price_in_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_cart_btn()
    page.solve_quiz_and_get_code()
    page.should_be_right_price()	

class TestUserAddToBasketFromProductPage():
# Функция SETUP    
    @pytest.fixture(scope='function', autouse = True)
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser,link)
        page.open()
        email = f"user_{time.time()}@fakemail.org"
        password = "TestPassword123"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_cart_btn()
        page.should_be_right_name_in_cart()
        page.should_be_right_price()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

class TestNegative():   
    
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_cart_btn()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
    
    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.click_add_to_cart_btn()
        page.should_disappeare_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
# Проверка пустоты корзины при переходе со страницы продукта
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_message()



