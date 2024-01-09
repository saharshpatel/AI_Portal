import pytest
from pages.profilepage import ProfilePage
from helper.policy_helper import PolicyHelper
import time

# To Run test parallel "pytest -n 4 /Users/******patel/PycharmProjects/AI_Portal/testcases/test_profile.py"
# To Run whole file individual use "pytest -k test_profile"


@pytest.mark.usefixtures("login")
def test_profile_phone_length_validation(login):
    profile_page = ProfilePage(login)
    policy_helper = PolicyHelper(login)
    policy_helper.cancel_policy_popup()
    time.sleep(1)
    profile_page.click_profile_section()
    time.sleep(1)
    profile_page.click_edit_button()
    time.sleep(1)
    profile_page.edit_phone("3244443555353555535555")
    time.sleep(1)
    profile_page.click_confirm_button()
    time.sleep(1)
    assert "Not more than 10 numbers" in login.page_source


@pytest.mark.usefixtures("login")
def test_profile_bio_length_validations(login):
    profile_page = ProfilePage(login)
    policy_helper = PolicyHelper(login)
    policy_helper.cancel_policy_popup()
    time.sleep(1)
    profile_page.click_profile_section()
    time.sleep(1)
    profile_page.click_edit_button()
    time.sleep(1)
    profile_page.edit_bio("This is a bio with more than 30 characters to test the length validation.")
    time.sleep(1)
    profile_page.click_confirm_button()
    time.sleep(1)
    assert "Not more than 30 characters" in login.page_source


@pytest.mark.usefixtures("login")
def test_profile_zip_code_length_validation(login):
    profile_page = ProfilePage(login)
    policy_helper = PolicyHelper(login)
    policy_helper.cancel_policy_popup()
    time.sleep(1)
    profile_page.click_profile_section()
    time.sleep(1)
    profile_page.click_edit_button()
    time.sleep(1)
    profile_page.edit_zip_code('1234567')
    time.sleep(1)
    profile_page.click_confirm_button()
    time.sleep(1)
    assert "Not more than 6 digits" in login.page_source


@pytest.mark.usefixtures("login")
def test_profile_clear_fields(login):
    profile_page = ProfilePage(login)
    policy_helper = PolicyHelper(login)
    policy_helper.cancel_policy_popup()
    time.sleep(1)
    profile_page.click_profile_section()
    time.sleep(1)
    profile_page.click_edit_button()
    time.sleep(1)
    profile_page.clear_phone_field()
    time.sleep(1)
    profile_page.clear_bio_field()
    time.sleep(1)
    profile_page.clear_zip_code_field()
    time.sleep(1)
    profile_page.click_confirm_button()
    assert "This field is required" in login.page_source

