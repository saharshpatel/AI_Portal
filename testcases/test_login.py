from pages.loginpage import LoginPage
import time
from helper.reporting_helper import take_screenshot, generate_html_report
from selenium.webdriver.common.by import By

# To run parallel test use "pytest -n 7 /Users/******patel/PycharmProjects/AI_Portal/testcases/test_login.py"


def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-sso.aithinkers.com')
    login_page.enter_credentials('xycndkjn.com', '********')
    login_page.click_login()
    assert "" in driver.page_source


def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-sso.aithinkers.com')
    login_page.enter_credentials('xyz@xyz', 'InvalidPassword')
    login_page.click_login()
    time.sleep(1)

    password_error_element = driver.find_element(By.XPATH, "//div[2]//div[3]")
    email_error_element = driver.find_element(By.XPATH, "//div//div//div[1]//div[3]")

    assert "Password must be 8 characters minimum, should include capital letters, numbers & special characters." in password_error_element.text
    assert "Please enter a valid email address." in email_error_element.text


def test_incorrect_password(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-sso.aithinkers.com')
    login_page.enter_credentials('xyz', 'IncorrectPassword123!')
    login_page.click_login()
    time.sleep(1)
    assert "Invalid Credentials" in driver.page_source


def test_password_length_limit(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-sso.aithinkers.com')
    login_page.enter_credentials('xyz.com', 'B@123hbhwbdchbhbhdnjschlhjbchbhss5659656565')
    login_page.click_login()
    time.sleep(1)
    assert "Invalid Credentials" in driver.page_source


def test_missing_email(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-sso.aithinkers.com')
    login_page.enter_credentials('', 'Test123!')
    login_page.click_login()
    time.sleep(1)
    assert "Email is required." in driver.page_source


def test_missing_password(setup):
    driver = setup
    login_page = LoginPage(driver)

    try:
        driver.get('https://dev-sso.aithinkers.com')
        login_page.enter_credentials('xyz@.com', '')
        login_page.click_login()
        time.sleep(1)
        assert "Password is required." in driver.page_source
# If assert failed then "it will take screenshot of failed test"
    except Exception as e:
        screenshot_path = take_screenshot(driver, "test_missing_password")
        html_report = generate_html_report("test_missing_password", f"Test failed: {e}\n\n{driver.page_source}")

        print(f"Test failed: {e}")
        print(f"Screenshot saved at: {screenshot_path}")
        print(f"HTML report saved at: {html_report}")
        raise e


def test_missing_email_and_password(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-sso.aithinkers.com')
    login_page.enter_credentials('', '')  # Empty email and password
    login_page.click_login()
    time.sleep(1)
    password_error_element = driver.find_element(By.XPATH, "//div[2]//div[3]")
    email_error_element = driver.find_element(By.XPATH, "//div//div//div[1]//div[3]")

    assert password_error_element.text == "Password is required."
    assert email_error_element.text == "Email is required."


