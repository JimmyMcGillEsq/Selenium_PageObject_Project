from .Pages.product_page import ProductPage
import pytest

# Ввел параметризацию - 10 тестовых страниц, одну пометил как ожидаемо падающую(XFail)
@pytest.mark.parametrize('promo', ['?promo=offer0', '?promo=offer1','?promo=offer2','?promo=offer3',
	'?promo=offer4','?promo=offer5','?promo=offer6',pytest.param('?promo=offer7', marks=pytest.mark.xfail(reason='Expected bug, wont be fixed')),'?promo=offer8','?promo=offer9'])
def test_guest_can_add_product_to_basket(browser, promo):
	link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{promo}'
	page = ProductPage(browser, link)
	page.open()
	page.click_add_to_cart_btn()
	page.solve_quiz_and_get_code()
	page.should_be_right_name_in_cart()
	page.should_be_right_price()

#def test_should_be_right_name_in_cart(browser):
#	page = ProductPage(browser, link)
#	page.open()
#	page.click_add_to_cart_btn()
#	page.solve_quiz_and_get_code()
#	page.should_be_right_name_in_cart()

#def test_should_be_right_price_in_cart(browser):
#    page = ProductPage(browser, link)
#    page.open()
#    page.click_add_to_cart_btn()
#    page.solve_quiz_and_get_code()
#    page.should_be_right_price()	
