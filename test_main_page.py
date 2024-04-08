#import pytest
#from selenium.webdriver.common.by import By
from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# Old School)
#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    browser.get(link)
#    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
#    login_link.click()

