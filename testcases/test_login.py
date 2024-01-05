from pages.loginpage import LoginPage
import time
from helper.reporting_helper import take_screenshot, generate_html_report


def test_valid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-portal.aithinkers.com/sign-in')
    login_page.click_sign_in()
    login_page.enter_credentials('sso.dev@aithinkers.com', 'Test123!')
    login_page.click_login()
    assert "" in driver.page_source


def test_invalid_login(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-portal.aithinkers.com/sign-in')
    login_page.click_sign_in()
    login_page.enter_credentials('invalid.user@aithinkers', 'InvalidPassword')
    login_page.click_login()
    time.sleep(1)
    assert "Please enter a valid email address." in driver.page_source


def test_incorrect_password(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-portal.aithinkers.com/sign-in')
    login_page.click_sign_in()
    login_page.enter_credentials('sso.dev@aithinkers.com', 'IncorrectPassword123!')
    login_page.click_login()
    time.sleep(1)
    assert "" in driver.page_source


def test_password_length_limit(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-portal.aithinkers.com/sign-in')
    login_page.click_sign_in()
    login_page.enter_credentials('sso.dev@aithinkers.com', 'B@123hbhwbdchbhbhdnjschlhjbchbhss5659656565')
    login_page.click_login()
    time.sleep(1)
    assert "" in driver.page_source


def test_missing_email(setup):
    driver = setup
    login_page = LoginPage(driver)
    driver.get('https://dev-portal.aithinkers.com/sign-in')
    login_page.click_sign_in()
    login_page.enter_credentials('', 'Test123!')
    login_page.click_login()
    time.sleep(1)
    assert "Email is required." in driver.page_source


def test_missing_password(setup):
    driver = setup
    login_page = LoginPage(driver)

    try:
        driver.get('https://dev-portal.aithinkers.com/sign-in')
        login_page.click_sign_in()
        login_page.enter_credentials('sso.dev@aithinkers.com', '')
        login_page.click_login()
        time.sleep(1)
        assert "Password is required.123" in driver.page_source

    except Exception as e:
        screenshot_path = take_screenshot(driver, "test_missing_password")
        html_report = generate_html_report("test_missing_password", f"Test failed: {e}\n\n{driver.page_source}")

        print(f"Test failed: {e}")
        print(f"Screenshot saved at: {screenshot_path}")
        print(f"HTML report saved at: {html_report}")
        raise e

