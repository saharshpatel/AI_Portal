import pytest
from pages.todopage import ToDoPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from helper.policy_helper import PolicyHelper
import time


@pytest.mark.usefixtures("login")
def test_todo_functionality(login):
    todo_page = ToDoPage(login)
    policy_helper = PolicyHelper(login)
    time.sleep(2)
    policy_helper.cancel_policy_popup()
    time.sleep(1)
    todo_page.click_expand_todo()
    time.sleep(2)
    todo_page.click_add_todo()
    time.sleep(2)
    todo_page.click_create_todo()
    time.sleep(2)
    todo_page.enter_todo_title("title16")
    time.sleep(2)
    todo_page.click_save_todo()
    time.sleep(2)
    todo_list_items = todo_page.get_todo_list_items()
    assert len(todo_list_items) == 1
    assert todo_list_items[0].text == "title16"
    todo_list_items[0].click()
    time.sleep(2)
    todo_page.enter_todo_description("This is an automated test description7")
    time.sleep(1)
    todo_page.press_enter_key(todo_page.todo_description_input)
    time.sleep(1)

    todo_list = WebDriverWait(login, 15).until(
        EC.presence_of_element_located(todo_page.todo_list_item)
    )
    todo_page.scroll_into_view(todo_list)
    ActionChains(login).move_to_element(todo_list).perform()

    time.sleep(1)
    todo_page.click_assign_unassign_button()
    todo_page.enter_assignment_search("saharsh")
    time.sleep(2)
    todo_page.select_assignment_result()
    time.sleep(2)

