from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PolicyHelper:
    def __init__(self, driver):
        self.driver = driver

    def cancel_policy_popup(self):
        try:
            cancel_button = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//*[name()='path' and contains(@d,'M19 6.41 1')]"))
            )
            cancel_button.click()
        except:
            pass

