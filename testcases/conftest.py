import pytest
from selenium import webdriver
from pages.loginpage import LoginPage


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-sso.aithinkers.com/')
    login_page.perform_login("sso.dev@aithinkers.com", "Test123!")
    return driver

