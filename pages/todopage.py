from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ToDoPage:
    def __init__(self, driver):
        self.driver = driver
        self.expand_todo_button = (By.XPATH, "//img[@alt='expand']")
        self.add_todo_button = (By.XPATH, "//div[@role='dialog']//div//div//div//div//form//div//div//div//*[name()='svg']//*[name()='path' and contains(@d,'M13 7h-2v4')]")
        self.create_todo_button = (By.XPATH, "//p[normalize-space()='Create Title']")
        self.todo_title_input = (By.XPATH, "//input[@placeholder='Enter the title']")
        self.todo_description_input = (By.XPATH, "//input[@placeholder='Enter the Description']")
        self.save_todo_button = (By.XPATH, "(//*[name()='svg'][@aria-label='save'])[1]")
        self.todo_list_item = (By.XPATH, "//body//div[@role='presentation']//ul[@role='menu']//div//div//div[1]//div[1]//div[1]//p[1]")
        self.assign_unassign_button = (By.XPATH, "//body//div[@role='presentation']//div[@role='dialog']//div//div//div//div//div[2]//div[1]//div[2]//*[name()='svg']//*[name()='path' and contains(@d,'M13 8c0-2.')]")
        self.assignment_search_field = (By.XPATH, "//input[@placeholder='Enter Employee Name']")
        self.assignment_result = (By.XPATH, "//body/div[@role='presentation']/div/ul[@role='menu']/div/div/div/div/span[1]")
        self.todo_item_locator = (By.XPATH, "/html[1]/body[1]/div[3]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/span[1]/input[1]")

    def click_expand_todo(self):
        expand_todo_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.expand_todo_button)
        )
        expand_todo_button.click()

    def click_add_todo(self):
        self.driver.find_element(*self.add_todo_button).click()

    def click_create_todo(self):
        self.driver.find_element(*self.create_todo_button).click()

    def enter_todo_title(self, title):
        todo_title_input = self.driver.find_element(*self.todo_title_input)
        todo_title_input.clear()
        todo_title_input.send_keys(title)

    def enter_todo_description(self, description):
        todo_description_input = self.driver.find_element(*self.todo_description_input)
        todo_description_input.clear()
        todo_description_input.send_keys(description)

    def click_save_todo(self):
        self.driver.find_element(*self.save_todo_button).click()

    def get_todo_list_items(self):
        todo_list_items = self.driver.find_elements(*self.todo_list_item)
        return todo_list_items

    def press_enter_key(self, element_locator):
        element = self.driver.find_element(*element_locator)
        element.send_keys(Keys.ENTER)

    def click_assign_unassign_button(self):
        assign_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.assign_unassign_button)
        )
        action = ActionChains(self.driver)
        action.move_to_element(assign_button).click().perform()

    def enter_assignment_search(self, search_text):
        assignment_search_field = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.assignment_search_field)
        )
        assignment_search_field.clear()
        assignment_search_field.send_keys(search_text)

    def select_assignment_result(self):
        assignment_result = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.assignment_result)
        )
        assignment_result.click()

    def hover_over_todo_list(self):
        todo_list = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.todo_list_item)
        )
        self.scroll_into_view(todo_list)
        ActionChains(self.driver).move_to_element(todo_list).perform()

    def scroll_into_view(self, element):
        ActionChains(self.driver).move_to_element(element).perform()
