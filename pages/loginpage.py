from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = (By.XPATH, "//button[text()='Sign In']")
        self.email_field = (By.ID, 'email-reg')
        self.password_field = (By.ID, 'password-reg')
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def click_sign_in(self):
        sign_in_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.sign_in_button))
        sign_in_button.click()

    def enter_credentials(self, email, password):
        email_field = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.email_field))
        email_field.clear()
        email_field.send_keys(email)

        password_field = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.password_field))
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.login_button))
        login_button.click()

    def perform_login(self, email, password):
        self.click_sign_in()
        self.enter_credentials(email, password)
        self.click_login()
