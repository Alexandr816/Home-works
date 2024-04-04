import pytest
from selenium import webdriver
from pages.registration import Register_Page,Auth_Page


@pytest.fixture(autouse=True,scope='class')
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def page(driver):
    page = Register_Page(driver)
    return page

@pytest.fixture(scope='function')
def page_a(driver):
    page_a = Auth_Page(driver)
    return page_a
