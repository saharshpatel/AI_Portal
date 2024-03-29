from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_section = (By.XPATH, "//a[@href='/profile']//div[@role='button']//div//span")
        self.edit_button = (By.XPATH, "//button[@type='button']//div//p")
        self.phone_input = (By.XPATH, "//input[@placeholder='Phone']")
        self.bio_textarea = (By.XPATH, "//input[@placeholder='Bio']")
        self.date_of_joining_calendar = (By.XPATH, "//input[@placeholder='Date Of Joining*']")
        self.date_of_birth_calendar = (By.XPATH, "//input[@placeholder='Date Of Birth*']")
        self.state_dropdown = (By.XPATH, "//select[@id='state']")
        self.city_dropdown = (By.XPATH, "//select[@id='city']")
        self.zip_code_input = (By.XPATH, "//input[@placeholder='Zip Code']")
        self.confirm_button = (By.XPATH, "//button[@title='Confirm']")
        self.upload_image_button = (By.XPATH, "//span[@role='button']//div//div")

    def click_profile_section(self):
        profile_section = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.profile_section))
        profile_section.click()

    def click_edit_button(self):
        edit_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.edit_button))
        edit_button.click()

    def edit_phone(self, phone):
        phone_input = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.phone_input))
        phone_input.clear()
        phone_input.send_keys(phone)

    def edit_zip_code(self, zip_code):
        zip_code_input = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.zip_code_input))
        zip_code_input.clear()
        zip_code_input.send_keys(zip_code)

    def edit_bio(self, bio):
        bio_textarea = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.bio_textarea))
        bio_textarea.clear()
        bio_textarea.send_keys(bio)

    def click_confirm_button(self):
        confirm_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.confirm_button))
        confirm_button.click()

    def clear_phone_field(self):
        phone_input = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.phone_input))
        phone_input.clear()
        phone_input.send_keys(Keys.BACKSPACE * 10)

    def clear_bio_field(self):
        bio_textarea = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.bio_textarea))
        bio_textarea.clear()
        bio_textarea.send_keys(Keys.BACKSPACE * 30)

    def clear_zip_code_field(self):
        zip_code_input = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable(self.zip_code_input))
        zip_code_input.clear()
        zip_code_input.send_keys(Keys.BACKSPACE * 6)
